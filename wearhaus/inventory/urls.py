from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('my-items', views.my_items, name='my-items'),
    path('all-items', views.all_items, name='all-items')
]
