from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("",include("hello_world.urls")),
    
    path("", include("my_blog.urls")),
    path("about/", include("my_blog.urls")),
    path("porfolio/", include("my_blog.urls")),
    path("contact/", include("my_blog.urls")),
]