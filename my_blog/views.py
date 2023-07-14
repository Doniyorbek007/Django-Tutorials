from django.shortcuts import render
from django.http import HttpResponse

def home(req):
    return render(req, "index.html")

def blog(req):
    return render(req,"blog.html")

def about(req):
    return render(req,"about.html")

def portfolio(req):
    return render(req, "portfolio.html")

def contact(req):
    return render(req, "contact.html")