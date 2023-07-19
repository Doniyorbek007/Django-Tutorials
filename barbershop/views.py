from django.shortcuts import render

# Create your views here.

def base(req):
    return render(req, 'base.html')

def home(req):
    return render(req, 'pages/section1.html')

def our_story(req):
    return render(req, 'pages/section2.html')

def sevices(req):
    return render(req, 'pages/section3.html')

def price_list(req):
    return render(req, 'pages/section4.html')

def contact(req):
    return render(req, 'pages/section5.html')