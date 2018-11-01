{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}
{% load humanize %}

{% block subject %}
[Check] {{ issue }}
{% endblock %}

{% block body %}
Here is the digest for you to review!
Update it by replying this email until *{{ issue.digest_date|date:"l" }} {{ issue.digest_date|date:"j"|ordinal }} at {{ issue.digest_date|date:"P" }}*.
*Note: Make sure to delete any quoted messages in your reply.*
-----

{{ issue.digest_text }}
{% endblock %}

{% block html %}
Here is the digest for you to review!<br/>
Update it by replying this email until <b>{{ issue.digest_date|date:"l" }} {{ issue.digest_date|date:"j"|ordinal }} at {{ issue.digest_date|date:"P" }}</b>.<br/>
<i>Note: Make sure to delete any quoted messages in your reply.</i><br>
<hr style="margin-bottom:1rem;"/>

{{ issue.digest_text|apply_markup:"markdown" }}
{% endblock %}
