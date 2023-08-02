from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View # import working for only this class
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
    barbers = Barber.objects.all()
    context = {
        'contact': contact,
        'branche': branche,
        'barbers': barbers
    }
    return render(req, 'pages/our_story.html',context)

def sevices(req):
    contact = Branche.objects.all()
    branche = Contact.objects.all()
    services = Service.objects.all()
    context = {
        'contact': contact,
        'branche': branche,
        'services': services,
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

# def contact(req):
#     contact = Branche.objects.all()
#     branche = Contact.objects.all()
#     context = {
#         'contact': contact,
#         'branche': branche,
#     }
#     return render(req, 'pages/contact.html',context)


# class ContactView(TemplateView):
#     models = Contact
#     template_name = 'pages/contact.html'

#     def render_data(self, **kwargs):
#         context = super(ContactView,self).get_context_data(self,**kwargs)
#         context ['contact'] = Contact.objects.all()
#         context ['branche'] = Branche.objects.all()

#         return context


class ContactView(TemplateView):
    models = Contact
