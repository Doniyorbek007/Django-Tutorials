from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Home</h1><div><a href='/home'style='margin-right:10px;'>Home</a><a href='/about'style='margin:10px;'>About</a><a href='/my_blog' style='margin:10px;'>My blog</a><a href='/porfolio'style='margin:10px;'>Portfolio</a><a href='/contact'style='margin:10px;'>Contact</a></div>")

def home(request):
    return HttpResponse("<h1>Home</h1><div><a href='/home'style='margin-right:10px;'>Home</a><a href='/about'style='margin:10px;'>About</a><a href='/my_blog' style='margin:10px;'>My blog</a><a href='/porfolio'style='margin:10px;'>Portfolio</a><a href='/contact'style='margin:10px;'>Contact</a></div>")

def about(request):
    return HttpResponse("<h1>About</h1><div><a href='/home'style='margin-right:10px;'>Home</a><a href='/about'style='margin:10px;'>About</a><a href='/my_blog' style='margin:10px;'>My blog</a><a href='/porfolio'style='margin:10px;'>Portfolio</a><a href='/contact'style='margin:10px;'>Contact</a></div>")

def my_blog(request):
    return HttpResponse("<h1>My blog</h1><div><a href='/home'style='margin-right:10px;'>Home</a><a href='/about'style='margin:10px;'>About</a><a href='/my_blog' style='margin:10px;'>My blog</a><a href='/porfolio'style='margin:10px;'>Portfolio</a><a href='/contact'style='margin:10px;'>Contact</a></div>")

def porfolio(request):
    return HttpResponse("<h1>Porfolio</h1><div><a href='/home'style='margin-right:10px;'>Home</a><a href='/about'style='margin:10px;'>About</a><a href='/my_blog' style='margin:10px;'>My blog</a><a href='/porfolio'style='margin:10px;'>Portfolio</a><a href='/contact'style='margin:10px;'>Contact</a></div>")

def contact(request):
    return HttpResponse("<h1>Contact</h1><div><a href='/home'style='margin-right:10px;'>Home</a><a href='/about'style='margin:10px;'>About</a><a href='/my_blog' style='margin:10px;'>My blog</a><a href='/porfolio'style='margin:10px;'>Portfolio</a><a href='/contact'style='margin:10px;'>Contact</a></div>")