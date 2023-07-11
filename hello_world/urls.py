from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="hello"),
    path("about/",views.about, name="about")
]