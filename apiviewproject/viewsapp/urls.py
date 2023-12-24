from django.urls import path
from . import views

urlpatterns = [
    path('API/', views.StudentAPI, name='home'),
]