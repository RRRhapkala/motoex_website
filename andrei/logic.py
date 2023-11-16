from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect, render
from andrei.models import Vehicle
from andrei.forms import VehicleForm
from andrei.exceptions import *


def register_user(request):
    user = User.objects.create(username=request.POST.get("username"))
    user.set_password(request.POST.get("password"))
    user.save()
    login(request, user)


def login_user(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('main')

    else:
        raise InvalidCridentialsException('Invalid email or password')


def add_vehicle(request):
    def user_can_add_vehicle(user):
        allowed_users = ['']
        return user.username in allowed_users

    if not user_can_add_vehicle(request.user):
        return render(request, 'main_page.html')

    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.users.add(request.user)
            vehicle.save()

            if 'main_image' in request.FILES:
                vehicle.main_image = request.FILES['main_image']
                vehicle.save()

            if 'additional_images' in request.FILES:
                for image in request.FILES.getlist('additional_images'):
                    vehicle.additional_images.create(image=image)

            return redirect('account')

# def toggle_like(vehicle_id, user):
#     vehicle_id = request.POST.get("vehicle_id")
#     vehicle = Vehicle.objects.get(id=vehicle_id)
#     vehicle.users.remove(request.user)
#     vehicle.save()
