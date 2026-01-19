from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Item


@require_http_methods(['GET'])
def inventory(request):
    return HttpResponse('Hello World')


@require_http_methods(['GET'])
def all_items(request):
    payload = list(Item.objects.values())
    return JsonResponse(payload, safe=False)


@login_required
@require_http_methods(['GET'])
def my_items(request):  # must be logged in
    payload = list(Item.objects.filter(user=request.user).values())
    return JsonResponse(payload, safe=False)


@csrf_exempt
@login_required
@require_http_methods(['POST'])
def create_item(request):  # must be logged in
    new_item = Item.objects.create(name=request.POST.get('name'),
                                   description=request.POST.get('description'),
                                   quantity=request.POST.get('quantity'),
                                   user=request.user
                                   )
    return JsonResponse({'message': 'successfully created item'})


@login_required
@require_http_methods(['GET'])
def read_item(request, pkid):  # must be your item
    # get full deets for editing
    payload = Item.objects.get(pk=pkid)
    if (payload.user != request.user):
        return JsonResponse({'message': 'You do not have permissions to edit this item'}, status=403)

    return JsonResponse(payload)


@login_required
@require_http_methods(['PUT'])
def update_item(request):  # must be your item

    pass


@login_required
@require_http_methods(['DELETE'])
def delete_item(request):  # must be your item

    pass
