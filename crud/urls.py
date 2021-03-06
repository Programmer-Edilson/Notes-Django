from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_notes, name="notes"),
    path('create/', views.create, name="create"),
    path('update/<int:pk>/', views.update, name="update"),
    path('delete/<int:pk>/', views.delete, name="delete"),
    path('profile/', views.profile, name="profile"),
    path('search/', views.search, name="search"),
]
