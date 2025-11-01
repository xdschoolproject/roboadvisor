# home_page/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page route
    path('stock-analysis/', views.stock_analysis, name='stock_analysis'),
]