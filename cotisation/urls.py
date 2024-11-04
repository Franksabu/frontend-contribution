from django.urls import path
from . import views

urlpatterns = [
    path("cotisations/list/", views.cotisation_list, name="cotisation_list"),
    path("cotisations/create/", views.cotisation_create, name="cotisation_create"),
    path("cotisations/<int:pk>/", views.cotisation_detail, name="cotisation_detail"),
]
