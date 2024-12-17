from django.urls import path
from cotisation import views

urlpatterns = [
    path("list/", views.cotisation_list, name="cotisation_list"),
    path("create/", views.cotisation_create, name="cotisation_create"),
    path("update/<int:id>/", views.cotisation_update, name="cotisation_update"),
    path("delete/<int:id>/", views.cotisation_delete, name="cotisation_delete"),
    path('cotisation/delete/<int:id>/', views.cotisation_delete, name='cotisation_delete'),
    path("detail/<int:pk>/", views.cotisation_detail, name="cotisation_detail"),
    path("contributions/list/", views.contribution_list, name="contribution_list"),
    path("contributions/create/", views.contribution_create, name="contribution_create"),
    path("contributions/update/<int:id>/", views.contributions_update, name="contributions_update"),
    path("contributions/delete/<int:id>/", views.contribution_delete, name="contributions_delete"),
    path("contributions/detail/<int:pk>/", views.contribution_detail, name="contribution_detail"),
    path("type_cotisations/list/", views.type_cotisation_list, name="type_cotisation_list"),
    path("type_cotisations/create/", views.type_cotisation_create, name="type_cotisation_create"),
    path("type_cotisation/delete/<int:id>/", views.type_cotisation_delete, name="type_cotisation_delete"),
    path("type_cotisation/update/<int:id>/", views.type_cotisation_update, name="type_cotisation_update"),
    path("type_cotisations/detail/<int:pk>/", views.type_cotisation_detail, name="type_cotisation_detail"),
    path("detail_contributions/list/", views.detail_contribution_list, name="detail_contribution_list"),
    path("detail_contributions/create/", views.detail_contribution_create, name="detail_contribution_create"),
    path("detail_contributions_detail/<int:pk>/", views.detail_contribution_detail, name="detail_contribution_detail"),
    path("detail_contributions/delete/<int:id>/", views.detail_contribution_delete, name="detail_contribution_delete"),
]
