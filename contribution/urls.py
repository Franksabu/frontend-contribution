from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("", include("membre.urls")),
    path("cotisation/", include("cotisation.urls")),
    path("", include("assistance.urls")),
    path("admin/", admin.site.urls),
]
