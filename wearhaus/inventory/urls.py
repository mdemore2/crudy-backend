from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('my-items', views.my_items, name='my-items'),
    path('all-items', views.all_items, name='all-items'),
    path("get-item/<int:pkid>", views.read_item,
         name="get-item"),  # <uuid:pkid>
    path('create-item', views.create_item, name='create-item'),
]
