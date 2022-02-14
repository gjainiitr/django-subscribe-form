from django.contrib import admin
from django.urls import path, include
from newsletter import views

urlpatterns = [
    path("subscribe", views.subscribe, name='subscribe'),
]