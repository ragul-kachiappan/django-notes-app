from django.urls import path, include
from . import views

app_name = "home_app"
urlpatterns = [
    path('', views.main_page, name = 'main_page'),
]