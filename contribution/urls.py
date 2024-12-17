from django.contrib import admin
from django.urls import path, include
from .views import home
urlpatterns = [
    path("", home, name="home"),
    path("membre/", include("membre.urls")),
    path("cotisation/", include("cotisation.urls")),
    path("assistance/", include("assistance.urls")),
    path("admin/", admin.site.urls),
]

