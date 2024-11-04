from django.urls import path
from . import views

urlpatterns = [
    path("detail_cotisations/list/", views.detail_cotisation_list, name="detail_cotisation_list"),
    path("detail_cotisations/create/", views.detail_cotisation_create, name="detail_cotisation_create"),
    path("detail_cotisations/<int:pk>/", views.detail_cotisation_detail, name="detail_cotisation_detail"),
]
