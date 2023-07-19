from django.shortcuts import render
from .models import Contact
# Create your views here.

def base(req):
    return render(req, 'base.html')

def home(req):
    return render(req, 'pages/home.html')

def our_story(req):
    return render(req, 'pages/our_story.html')

def sevices(req):
    return render(req, 'pages/services.html')

def price_list(req):
    return render(req, 'pages/price_list.html')

def contact(req):
    data = 
    return render(req, 'pages/contact.html')