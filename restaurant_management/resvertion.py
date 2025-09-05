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

body{
    margin:0;
    padding:0;
    front-family:Arial,helvetica,sams-serif;
    background-color:#f9f9f9f
    color:#333
}
header{
    background-color:white;
    color:black;
    text-algin:center;
    padding:1,5rem;
}
h1{
    margin:0;
    font-size:2,rem;
}
main{
    padding:2rem;
    max-width:900;
    margin:0 auto;
}
p{
    font-size:1.1rem;
    line-heigth:1.6;
    margin-bottom:1rem;
}
a{
    color:black;
    text-decoration:underline;
}
a:hover{
    text-decoration:underline;
}
footer{
    margin-top:2rem;
    background:blue;
    color:white;
    text-algin:cenetr;
    padding:1rem;
    font-size:0,8rem;
}