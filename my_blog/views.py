# from django.http import HttpResponse,JsonResponse
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Contact, Blog

def home(req):
    # return HttpResponse("<h1>Home</h1>")
    # return JsonResponse({"userId": 1})
    context = {'name': 'Sardor'}
    return render(req, "pages/home.html", context)

def about(req):
    return render(req, "pages/about.html")

def portfolio(req):
    return render(req, "pages/portfolio.html")  

def blog(req):
    return render(req, "pages/blog.html")

class BlogPageView(ListView):
    model = Blog
    template_name = 'pages/blog.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context["blog"] = Blog.objects.all()
        return context
    
class DetailBlogView(DetailView):
    model = Blog
    template_name = 'pages/blog_single.html'
    

def contact(req):
    data = Contact.objects.all()
    context = {"data":data}
    return render(req, "pages/contact.html",context)