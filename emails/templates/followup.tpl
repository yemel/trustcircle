{% extends "update.tpl" %}
{% load markup_tags %}

{% block subject %}
Call for updates: {{ issue }}
{% endblock %}

{% block body %}
Hey, this is a friendly reminder! You have until XXXX to answer.
{% endblock %}

{% block html %}
Hey, this is a friendly reminder! You have until XXXX to answer.
{% endblock %}
