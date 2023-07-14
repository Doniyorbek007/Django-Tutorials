from django.shortcuts import render
# from django.http import HttpResponse

def home(req):
    context = {'name':'Sardor'} 
    return render(req, "pages/home.html", context)

def blog(req):
    return render(req,"pages/blog.html")

def about(req):
    return render(req,"pages/about.html")

def portfolio(req):
    return render(req, "pages/portfolio.html")

def contact(req):
    return render(req, "pages/contact.html")