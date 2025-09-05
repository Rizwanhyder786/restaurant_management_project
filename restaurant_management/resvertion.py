{% extends "base.html" %}  {# remove this line if you don't have a base,html yet}
{ % block content %}
    <div style="display:flex;" justfiy-content:center; algin-items:center; 
     <h1>resverytion</h1>
     <p>resverytion system coming soon</p>
    </div>
{% endblock %}
from datatime import datatime
def current_year(request):
    return{
        'year':datetime.now().year
    }

