from django.urls import path
from .views import ContactView
from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("our-story/", views.our_story, name="our-story"),
    path("services/", views.sevices, name="services"),
    path("price-list/", views.price_list, name="price-list"),
    # path("contact/", views.contact, name="contact"),
    path('contact/', ContactView.as_view(),name='contact')
]
