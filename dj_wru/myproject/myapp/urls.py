from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_phone_number, name='search_phone_number'),
]
