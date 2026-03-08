---
layout: default
title: 每日AI新闻速递
---


## 中文速递 [订阅]({{ '/feed.xml' | relative_url }})

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

## English Digest [Subscribe]({{ '/feed.xml' | relative_url }})

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
