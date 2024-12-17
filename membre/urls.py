from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.membre_list, name="membre_list"),
    path("membres/create/", views.membre_create, name="membre_create"),
    path("membres/<int:pk>/", views.membre_detail, name="membre_detail"),
    path("membres/<int:id>/update/", views.membre_update, name="membre_update"),
    path('membre/delete/<int:id>/', views.membre_delete, name='membre_delete'),
    path("membres/<int:pk>/validate/", views.membre_validate, name="membre_validate"),
    path('', views.index_view, name='index_view'),
]
