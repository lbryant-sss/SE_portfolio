import posixpath
from django.contrib import admin
from django.urls import path, include
from . views import homeView

urlpatterns = [
    path('', homeView.as_view(), name='home'),
]