from django.contrib import admin
from django.urls import path
from .views import helloWorldview

urlpatterns = [
    path('', helloWorldview),
]
