from django.urls import path
from . import views

urlpatterns = [
    path('', views.managers, name='managers'),
    path('register', views.register, name='register')
]
