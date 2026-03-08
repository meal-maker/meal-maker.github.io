---
layout: default
title: 每日AI新闻速递
---


## 中文速递 <a class="rss-icon" href="{{ '/feed-zh.xml' | relative_url }}" aria-label="订阅中文"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6 17a2 2 0 11-.001-4.001A2 2 0 016 17zm-2-9.5v3A8.5 8.5 0 0112.5 19h3A11.5 11.5 0 014 7.5zm0-4v3A12.5 12.5 0 0116.5 19h3C19.5 9.784 12.216 2.5 4 2.5z"/></svg></a>

<ul>
  {% assign zh_posts = site.posts | where: "lang", "zh" %}
  {% for post in zh_posts limit:20 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a>
    </li>
  {% else %}
    <li><em>暂无内容</em></li>
  {% endfor %}
</ul>

## English Digest <a class="rss-icon" href="{{ '/feed-en.xml' | relative_url }}" aria-label="Subscribe English"><svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M6 17a2 2 0 11-.001-4.001A2 2 0 016 17zm-2-9.5v3A8.5 8.5 0 0112.5 19h3A11.5 11.5 0 014 7.5zm0-4v3A12.5 12.5 0 0116.5 19h3C19.5 9.784 12.216 2.5 4 2.5z"/></svg></a>

<ul>
  {% assign en_posts = site.posts | where: "lang", "en" %}
  {% for post in en_posts limit:20 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.date | date: "%Y-%m-%d" }}</a>
    </li>
  {% else %}
    <li><em>No posts yet</em></li>
  {% endfor %}
</ul>
