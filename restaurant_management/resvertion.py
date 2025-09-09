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
STATIC_URL="/static/"
import os
STATICFILES_DIRS=[
    os.Path.join(BASE_DIR,"myapp/static"),
]
from django.shortcuts import render
from django.http import JsonResponse
from django.db import DatabaseError
from .models import Customer

def customer_list(request):
    try:
        customers = Customer.objects.all()
        data = {"customers": list(customers.values("id", "name", "emsil"))}
        return JsonResponse(data,safe=Flase)
    except DatabaseError as e:
        return JsonResponse({"error":"database error occurred.please try again later"},status=500)
    except Exception as e:
        return JsonResponse)({"error":"An unexpeted error occurred."},status=500)
<!DOCTYPE html>
<head>
 <meta charset="UTF-8">
 <tittle>Contact From</tittle>
 </head>
 <body>
 <h2>Contact From</h2>
 <from id ="contact from">
 <label for ="name">Name:</label>
 <input type="text" id="email" name="name"><br>
 <label for="email" > Email:</label><br>
 <input type="submit">Submit</button>
 </from>
 <p> id="errorMessage" style="color:red"></p>
 <scrpit>
 document.getElementByld("contactfrom").addeventlistner("submit",function(event){
    const name=
 document.getElementByld("name").value.trim();
    const email=
 document.getElementByld("email").value.trim();
    const errorMessage=
 document.getElementByld("errorMessage");
    if (name===""|| email===""){
        errorMessage.textcontent = "please fill in both name and email fields";
        event.preventDefault();
        } else{
            errorMessage.textcontent="";
        }
 });
 </scrpit>
 </body>
 </html>

 <footer style="text-algin:center;margin-top:20px;
 padding:10px;background:blue;">
 <p>&copy;{{year}} your restaurant name</p>
 <p>opening hours:mon-fri:11am-9pm,sat-sun:10am-10pm</p>
 </footer>

 # yourapp/views.py
 from django.shortcuts import render
 from .froms import searchfrom

 def homepage(request):
    from =sreachfrom(request.GET or None)
    #no search logic yet,
    return render(request,"homepage.html",{"from":from})
    ------------------------------------------------------
    from django.db import models
    class feedback(models.model):
        comment = models.textfeild()
        created_at = models.datatimefeild(auto_now_add=True)

        def __str__(self):
            return f"feedback {self.id} - {self.created_at.strftime(%Y-%d%H.%M)}"
            ---------------------------------------------------------------------
            import datatime
            def current_year(request):
                return{
                    'year':datatime.datatime.now().year
                }