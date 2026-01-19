from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, QueryDict
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from .models import Item
import json


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


@csrf_exempt
@login_required
@require_http_methods(['PUT'])
def edit_item(request, pkid):  # must be your item
    data = json.loads(request.body)
    target = Item.objects.get(pk=pkid)
    if (target.user != request.user):
        return JsonResponse({'message': 'You do not have permissions to edit this item'}, status=403)
    target.name = data['name']
    target.description = data['description']
    target.quantity = data['quantity']
    target.save()

    # Item.objects.filter(pk=pkid).update(
    #    name=request.POST.get('name'),
    #    description=request.POST.get('description'),
    #    quantity=request.POST.get('quantity'),
    # )
    return JsonResponse({'message': 'Update complete'}, status=202)


@csrf_exempt
@login_required
@require_http_methods(['DELETE'])
def delete_item(request):  # must be your item

    pass

# @login_required
# @require_http_methods(['GET'])
# def read_item(request, pkid):  # must be your item
#    # get full deets for editing
#    target = Item.objects.get(pk=pkid)
#    if (target.user != request.user):
#        return JsonResponse({'message': 'You do not have permissions to edit this item'}, status=403)
#
#    return JsonResponse(target)
