from django.urls import path
from . import views

urlpatterns = [
    path('webgl/', views.webgl, name='webgl'),
    path('', views.index, name='index'),
]

