from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    path('delete/', views.delete, name="delete_user"),

]
