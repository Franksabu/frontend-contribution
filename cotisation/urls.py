from django.urls import path
from cotisation import views

urlpatterns = [
    path("list/", views.cotisation_list, name="cotisation_list"),
    path("create/", views.cotisation_create, name="cotisation_create"),
    path("<int:pk>/", views.cotisation_detail, name="cotisation_detail"),
    path("contributions/list/", views.contribution_list, name="contribution_list"),
    path("contributions/create/", views.contribution_create, name="contribution_create"),
    path("contributions/<int:pk>/", views.contribution_detail, name="contribution_detail"),
    path("type_cotisations/list/", views.type_cotisation_list, name="type_cotisation_list"),
    path("type_cotisations/create/", views.type_cotisation_create, name="type_cotisation_create"),
    path("type_cotisations/<int:pk>/", views.type_cotisation_detail, name="type_cotisation_detail"),
    path("detail_contributions/list/", views.detail_contribution_list, name="detail_contribution_list"),
    path("detail_contributions/create/", views.detail_contribution_create, name="detail_contribution_create"),
    path("detail_contributions_detail/<int:pk>/", views.detail_contribution_detail, name="detail_contribution_detail"),
]
