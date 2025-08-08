from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
#login view
def login_view(request):
    return HttpResponse("this is the login page.")
#resister view
def resister_view(request):
    return HttpResponse("This is the Registration page.")
#profile view
def profile_view(request):
    return HttpResponse("this is the user profile page")
