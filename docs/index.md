---
layout: default
title: 每日AI新闻速递
---


## 中文速递 <a class="rss-icon" href="{{ '/feed-zh.xml' | relative_url }}" aria-label="订阅中文">📡</a>

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

## English Digest <a class="rss-icon" href="{{ '/feed-en.xml' | relative_url }}" aria-label="Subscribe English">📡</a>

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
