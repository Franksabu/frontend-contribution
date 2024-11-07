from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path("", home, name="home"),
    path("membres/", include("membre.urls")),
    path("cotisations/", include("cotisation.urls")),
    path("assistances/", include("assistance.urls")),
    path("admin/", admin.site.urls),
]
