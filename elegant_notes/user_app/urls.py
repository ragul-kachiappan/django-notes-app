from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register_page, name= 'register'),
    path('login/', views.login_page, name= 'login'),
]