from django.shortcuts import render

# Create your views here.
def home(req):
    return render(req,'base.html')

def about(req):
    return render(req, 'pages/about.html')

def doctor(req):
    return render(req, 'pages/doctor.html')

def departments(req):
    return render (req, 'pages/departments.html')

def pricing(req):
    return render(req, 'pages/pricing.html')

def blog(req):
    return render(req, 'pages/blog.html')

def contact(req):
    return render(req, 'pages/contact.html')