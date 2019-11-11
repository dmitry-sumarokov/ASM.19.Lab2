{% extends "base.tpl" %}

{% block content %}
It is magic!<br>
The cat's saying:<br>
{{ o._cat.do_meow() }}<br>
<a href="/">Back</a><br>
{% endblock %}

