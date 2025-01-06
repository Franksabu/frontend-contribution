from django.urls import path
from . import views

urlpatterns = [
    path("assistances/list/", views.assistance_list, name="assistance_list"),
    path("assistances/create/", views.assistance_create, name="assistance_create"),
    path("assistances/detail/<int:pk>/", views.assistance_detail, name="assistance_detail"),
    path("assistances/update/<int:id>/", views.assistance_update, name="assistance_update"),
    path("assistances/delete/<int:id>/", views.assistance_delete, name="assistance_delete"),
]
