from django.urls import path
from . import views

urlpatterns = [
    path("membres/list/", views.membre_list, name="membre_list"),
    path("membres/create/", views.membre_create, name="membre_create"),
    path("membres/<int:pk>/", views.membre_detail, name="membre_detail"),
    # path("get-choices/", views.get_choices, name="get_choices"),
    path("membres/<int:pk>/update/", views.membre_update, name="membre_update"),
    path("membres/<int:pk>/delete/", views.membre_delete, name="membre_delete"),
    path("membres/<int:pk>/validate/", views.membre_validate, name="membre_validate"),
]
