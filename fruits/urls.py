# fruits/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_fruit_set, name='add_fruit_set'),
    path('search/', views.search_fruit_set, name='search_fruit_set'),
    path('', views.dashboard, name='dashboard'),  # Dashboard URL

]
