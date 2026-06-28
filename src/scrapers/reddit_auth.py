"""OAuth2 token management for authenticated Reddit access.

Fetches and caches a bearer token via the script-app password grant so that
listing/comment requests to ``oauth.reddit.com`` succeed where anonymous
data-center IPs get 403'd. The token is cached in memory for the lifetime of
a single run; if fetching fails the manager returns ``None`` so callers can
gracefully fall back to the anonymous RSS path.
"""

import logging
from datetime import datetime, timedelta, timezone
from typing import Optional

import httpx

from ..models import RedditAuthConfig

logger = logging.getLogger(__name__)

TOKEN_URL = "https://www.reddit.com/api/v1/access_token"
# Refresh a little before the real expiry to avoid racing the clock.
EXPIRY_MARGIN = timedelta(seconds=60)


class RedditTokenManager:
    """Fetches and caches an OAuth2 bearer token (password grant)."""

    def __init__(self, auth: RedditAuthConfig, http_client: httpx.AsyncClient):
        self._auth = auth
        self._client = http_client
        self._token: Optional[str] = None
        self._expires_at: Optional[datetime] = None

    def _resolve_credentials(self) -> Optional[tuple[str, str, str, str]]:
        """Read secrets from the environment; return None if any are missing."""
        import os

        client_id = os.getenv(self._auth.client_id_env)
        client_secret = os.getenv(self._auth.client_secret_env)
        password = os.getenv(self._auth.password_env)
        if not client_id or not client_secret or not password:
            logger.warning(
                "Reddit OAuth env vars not fully set "
                "(need %s, %s, %s); falling back to anonymous access",
                self._auth.client_id_env,
                self._auth.client_secret_env,
                self._auth.password_env,
            )
            return None
        return client_id, client_secret, self._auth.username, password

    def _user_agent(self) -> str:
        if self._auth.user_agent:
            return self._auth.user_agent
        return f"horizon:1.0 (by /u/{self._auth.username})"

    async def get_token(self) -> Optional[str]:
        """Return a cached bearer token, or fetch a fresh one if absent/expired.

        Returns None on any failure (missing env, network error, non-2xx) so
        the caller can degrade to anonymous access.
        """
        if self._token and self._expires_at and datetime.now(timezone.utc) < self._expires_at:
            return self._token

        creds = self._resolve_credentials()
        if not creds:
            return None
        client_id, client_secret, username, password = creds

        try:
            response = await self._client.post(
                TOKEN_URL,
                data={
                    "grant_type": "password",
                    "username": username,
                    "password": password,
                },
                auth=(client_id, client_secret),
                headers={"User-Agent": self._user_agent()},
            )
        except httpx.HTTPError as e:
            logger.warning("Reddit token request failed: %s", e)
            return None

        if response.status_code != 200:
            logger.warning(
                "Reddit token endpoint returned %s: %s",
                response.status_code,
                response.text[:200],
            )
            return None

        try:
            payload = response.json()
            token = payload["access_token"]
            expires_in = int(payload.get("expires_in", 3600))
        except (ValueError, KeyError) as e:
            logger.warning("Reddit token response was malformed: %s", e)
            return None

        self._token = token
        self._expires_at = datetime.now(timezone.utc) + timedelta(
            seconds=expires_in
        ) - EXPIRY_MARGIN
        logger.info("Reddit OAuth token acquired (expires in %ds)", expires_in)
        return self._token
