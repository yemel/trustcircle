{% extends "update.tpl" %}
{% load markup_tags %}
{% load humanize %}

{% block subject %}
Call for updates: {{ issue }}
{% endblock %}

{% block body %}
Friendly reminder, please answer before *{{ issue.digest_date|date:"l" }} {{ issue.digest_date|date:"j"|ordinal }} at {{ issue.digest_date|date:"P" }}*.
{% endblock %}

{% block html %}
Friendly reminder, please answer before <b>{{ issue.digest_date|date:"l" }} {{ issue.digest_date|date:"j"|ordinal }} at {{ issue.digest_date|date:"P" }}</b>.
{% endblock %}
