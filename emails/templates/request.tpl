{% extends "mail_templated/base.tpl" %}
{% load markup_tags %}

{% block subject %}
[Check] Call for updates: {{ issue }}
{% endblock %}

{% block body %}
Hey, please write the call for updates below.
{% endblock %}

{% block html %}
Hey, please write the call for updates below.
{% endblock %}
