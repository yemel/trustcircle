{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}
{% load humanize %}

{% block subject %}
Call for updates: {{ message.issue }}
{% endblock %}

{% block body %}
Got it! Find below a copy of your message.
Update it by replying this email until *{{ issue.digest_date|date:"l" }} {{ issue.digest_date|date:"j"|ordinal }} at {{ issue.digest_date|date:"P" }}*.
-----

{{ message.data_text }}
{% endblock %}

{% block html %}
Got it! Find below a copy of your message.<br/>
Update it by replying to this email until <b>{{ issue.digest_date|date:"l" }} {{ issue.digest_date|date:"j"|ordinal }} at {{ issue.digest_date|date:"P" }}</b>.<br/>
<hr style="margin-bottom:1rem;"/>

{{ message.data_text|apply_markup:"markdown" }}
{% endblock %}
