{% extends "mail_templated/base.tpl" %}

{% block subject %}
[Check] {{ issue }}
{% endblock %}

{% block body %}
I'm going to send this digest:
-----

{{ issue.digest_text }}
{% endblock %}

{% block html %}
I'm going to send this digest:<br/>
<hr style="margin-bottom:1rem;"/>

{{ issue.get_digest_html|safe }}
{% endblock %}
