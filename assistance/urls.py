from django.urls import path
from . import views

urlpatterns = [
    path("assistances/list/", views.assistance_list, name="assistance_list"),
    path("assistances/create/", views.assistance_create, name="assistance_create"),
    path("assistances/<int:pk>/", views.assistance_detail, name="assistance_detail"),
]