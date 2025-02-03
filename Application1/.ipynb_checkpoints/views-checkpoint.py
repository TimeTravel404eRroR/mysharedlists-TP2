from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Index of shared list')
# Modifier le fichier your_project > urls.py

from django.contrib import admin
from django.urls import path
from Application1 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index')
]