{% extends "mail_templated/base.tpl" %}

{% block subject %}
Call for updates: {{ issue }}
{% endblock %}

{% block body %}
Got it, I'm going to send this update:
-----

{{ message.data_html }}
{% endblock %}

{% block html %}
I'm going to send this update:<br/>
-----<br/><br/>

{{ message.get_html|safe }}
{% endblock %}
