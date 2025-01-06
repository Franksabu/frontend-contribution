from .views import home
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include
from .views import login_view, register_view, logout_view
# from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", lambda request: redirect('login')),
    path("admin/", admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path("home/", home, name="home"),
    path("membre/", include("membre.urls")),
    path("cotisation/", include("cotisation.urls")),
    path("assistance/", include("assistance.urls")),
]
