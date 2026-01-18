from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


def managers(request):
    return HttpResponse('Hello World')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

    user = User.objects.filter(username=username)
    if user.exists():
        return JsonResponse({'error': 'User already exists'}, status=409)

    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username
    )
    user.set_password(password)
    user.save()

    return JsonResponse({'message': 'User created. Please login.'}, status=201)


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({'message': 'Login successful.'}, status=200)


def logout_user(request):
    logout(request)
    return JsonResponse({'message': 'Logout successful.'}, status=200)
