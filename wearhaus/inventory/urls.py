from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('my-items', views.my_items, name='my-items'),
    path('all-items', views.all_items, name='all-items'),
    path('create-item', views.create_item, name='create-item'),
    path('edit-item/<int:pkid>', views.edit_item, name='edit-item')
]
