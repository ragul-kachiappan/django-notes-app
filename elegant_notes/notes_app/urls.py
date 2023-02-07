from django.urls import path, include
from . import views

app_name = "notes_app"
urlpatterns = [
    path('', views.home_view, name = 'home'),
]