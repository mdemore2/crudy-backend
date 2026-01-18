from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Item


def inventory(request):
    return HttpResponse('Hello World')


def all_items(request):
    payload = list(Item.objects.values())
    return JsonResponse(payload)


def my_items(request):  # must be logged in

    return JsonResponse({})


def create_item(request):  # must be logged in
    pass


def read_item(request):  # must be your item

    # get full deets for editing
    pass


def update_item(request):  # must be your item

    pass


def delete_item(request):  # must be your item

    pass
