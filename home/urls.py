from django.urls import path
from .views import * # import your viewa.py

urlpatterns = [:
    path(",view.home,name=home"),   #URL:handled by views.home
    path('about/',view.about,name='about'),  #URL:about 
]