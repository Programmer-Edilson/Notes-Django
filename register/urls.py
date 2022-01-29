from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name="signup"),
    #path('update/', views.update, name="update_user"),
    path('delete/', views.delete, name="delete_user"),

]
