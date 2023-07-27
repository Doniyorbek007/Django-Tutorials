from django.shortcuts import render
from .models import *
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
    price = Price.objects.all()
    context = {'price' : price} 
    return render(req, 'pages/price_list.html',context)

def contact(req):
    contact = Branche.objects.all()
    branche = Contact.objects.all()
    context = {
        'contact': contact,
        'branche': branche,
    }
    return render(req, 'pages/contact.html',context)