from django.urls import path, include
from . import views

app_name = "notes_app"
urlpatterns = [
    path('', views.home_view, name = 'home'),
    path('delete/<int:pk>', views.delete_view, name = 'delete'),
    path('create/', views.create_view, name = 'create'),
    path('update/<int:pk>', views.update_view, name = 'update')

]