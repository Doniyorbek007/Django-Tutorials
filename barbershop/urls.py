from django.urls import path

from . import views

urlpatterns = [
    path("", views.base, name="base"),
    path("home/", views.home, name="home"),
    path("our-story/", views.our_story, name="our-story"),
    path("services/", views.sevices, name="services"),
    path("price-list/", views.price_list, name="price-list"),
    path("contact/", views.contact, name="contact"),
]
