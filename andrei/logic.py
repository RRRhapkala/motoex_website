from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import redirect
from andrei.models import Vehicle
from andrei.forms import VehicleForm
from andrei.exceptions import *


def register_user(request):
    user = User.objects.create(username=request.POST.get("username"))
    user.set_password(request.POST.get("password"))
    user.save()
    login(request, user)


def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('main')

    else:
        raise InvalidCridentialsException('Invalid email or password')


def add_vehicle(request):
    vehicle_form = VehicleForm(request.POST)
    if vehicle_form.is_valid():
        vehicle_form.save()
    else:
        raise InvalidVehicleFormException(vehicle_form.errors)


# def toggle_like(vehicle_id, user):
#     vehicle_id = request.POST.get("vehicle_id")
#     vehicle = Vehicle.objects.get(id=vehicle_id)
#     vehicle.users.remove(request.user)
#     vehicle.save()