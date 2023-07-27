from django.shortcuts import render
from .models import *
# Create your views here.

def base(req):
    contact = Branche.objects.all()
    branche = Contact.objects.all()
    context = {
        'contact': contact,
        'branche': branche,
    }
    return render(req, 'base.html',context)

def home(req):
    contact = Branche.objects.all()
    branche = Contact.objects.all()
    context = {
        'contact': contact,
        'branche': branche,
    }
    return render(req, 'pages/home.html',context)

def our_story(req):
    contact = Branche.objects.all()
    branche = Contact.objects.all()
    context = {
        'contact': contact,
        'branche': branche,
    }
    return render(req, 'pages/our_story.html',context)

def sevices(req):
    contact = Branche.objects.all()
    branche = Contact.objects.all()
    context = {
        'contact': contact,
        'branche': branche,
    }
    return render(req, 'pages/services.html',context)

def price_list(req):
    contact = Branche.objects.all()
    branche = Contact.objects.all()
    price = Price.objects.all()
    context = {
    'price' : price,
    'contact': contact,
    'branche': branche,   
    } 
    return render(req, 'pages/price_list.html',context)

def contact(req):
    contact = Branche.objects.all()
    branche = Contact.objects.all()
    context = {
        'contact': contact,
        'branche': branche,
    }
    return render(req, 'pages/contact.html',context)