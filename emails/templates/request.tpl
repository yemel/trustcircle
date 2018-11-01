{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}
{% load humanize %}

{% block subject %}
[Write] Call for updates: {{ issue }}
{% endblock %}

{% block body %}
Please write a message requesting news to the *{{ issue.circle.name }}* circle members.
Remember to include some kick-off questions.

You have time until *{{ issue.request_date|date:"l" }} {{ issue.request_date|date:"j"|ordinal }} at {{ issue.request_date|date:"P" }}* to answer this email.
{% endblock %}

{% block html %}
Please write a message requesting news to the <i>{{ issue.circle.name }}</i> circle members.<br/>
It's always recommended to include some kick off questions.<br/><br/>

You have time until <b>{{ issue.request_date|date:"l" }} {{ issue.request_date|date:"j"|ordinal }} at {{ issue.request_date|date:"P" }}</b> to answer this email.
{% endblock %}
