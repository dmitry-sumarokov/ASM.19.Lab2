{% extends "base.tpl" %}

{% block content %}
<form action='/AddItem' method=POST>
<input type=hidden name=id value={{id}}>
Name: <input type=text name=name value="{{o._name}}"><br>
Gender: <input type=text name=gender value="{{o._gender}}"><br>
Age: <input type=number name=age value="{{o._age}}"><br>
Colour: <input type=text name=colour value="{{o._colour}}"><br>
<input type=submit value=" Ok "><br>
</form>

{% endblock %}
