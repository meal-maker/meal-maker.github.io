---
layout: default
title: 每日AI新闻速递
---


<div class="title-row">
  <h2>中文速递</h2>
  <a class="subscribe-icon" href="{{ '/feed-zh.xml' | relative_url }}" aria-label="订阅中文"></a>
</div>

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

<div class="title-row">
  <h2>English Digest</h2>
  <a class="subscribe-icon" href="{{ '/feed-en.xml' | relative_url }}" aria-label="Subscribe English"></a>
</div>

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
