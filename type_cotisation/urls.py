from django.urls import path
from . import views
urlpatterns = [
    path("type_cotisations/list/", views.type_cotisation_list, name="type_cotisation_list"),
    path("type_cotisations/create/", views.type_cotisation_create, name="type_cotisation_create"),
    path("type_cotisations/<int:pk>/", views.type_cotisation_detail, name="type_cotisation_detail")
]
