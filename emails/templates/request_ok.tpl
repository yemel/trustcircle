{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}
{% load humanize %}

{% block subject %}
[Check] Call for updates: {{ issue }}
{% endblock %}

{% block body %}
Got it! Find below a copy of your message.
Update it by replying to this email until *{{ issue.request_date|date:"l" }} {{ issue.request_date|date:"j"|ordinal }} at {{ issue.request_date|date:"P" }}*.
-----

{{ issue.request_text }}
{% endblock %}

{% block html %}
Got it! Find below a copy of your message.<br/>
Update it by replying to this email until <b>{{ issue.request_date|date:"l" }} {{ issue.request_date|date:"j"|ordinal }} at {{ issue.request_date|date:"P" }}</b>.<br/>
<hr style="margin-bottom:1rem;"/>

{{ issue.request_text|apply_markup:"markdown" }}
{% endblock %}
