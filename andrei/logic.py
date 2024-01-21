from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect
from andrei.models import Vehicle, MainImage, AdditionalImage
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

def user_can_add_vehicle(user):
        allowed_users = ['ggoutsiderr', 'a2']
        return user.username in allowed_users

def edit_vehicle(request, vehicle):
    if not user_can_add_vehicle(request.user):
        raise UCantAddVehicle('Fuck off bozo')
    
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()

            if 'main_image' in request.FILES:
                MainImage.objects.get(vehicle=vehicle).delete()

                vehicle_main_image = MainImage.objects.create(
                    image=request.FILES.get('main_image'),
                    vehicle=vehicle
                )
                vehicle_main_image.save()

            if 'additional_images' in request.FILES:
                AdditionalImage.objects.filter(vehicle=vehicle).delete()

                for image in request.FILES.getlist('additional_images'):
                    vehicle_additional_image = AdditionalImage.objects.create(
                        image=image,
                        vehicle=vehicle
                    )
                    vehicle_additional_image.save()


def add_vehicle(request):

    if not user_can_add_vehicle(request.user):
        raise UCantAddVehicle('Fuck off bozo')

    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.save()

            if 'main_image' in request.FILES:
                vehicle_main_image = MainImage.objects.create(
                    image=request.FILES.get('main_image'),
                    vehicle=vehicle
                )
                vehicle_main_image.save()

            if 'additional_images' in request.FILES:
                for image in request.FILES.getlist('additional_images'):
                    vehicle_additional_image = AdditionalImage.objects.create(
                        image=image,
                        vehicle=vehicle
                    )
                    vehicle_additional_image.save()


def get_liked_vehicles_for_user(request):
    liked_vehicles = Vehicle.objects.filter(users__id__contains=request.user.id)
    return liked_vehicles

def get_user_like_vehicle_class(request, vehicle: Vehicle):
    if not request.user.is_authenticated:
        return 'like-vehicle-nonpressed'
    
    return 'like-vehicle-pressed' \
        if vehicle.users.filter(id=request.user.id).exists() \
        else 'like-vehicle-nonpressed'

def toggle_like(user: User, vehicle: Vehicle):
    if vehicle is None:
        return
    
    if vehicle.users.filter(id=user.id).exists():
        vehicle.users.remove(user)
    else:
        vehicle.users.add(user)
