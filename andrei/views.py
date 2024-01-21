from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from andrei.exceptions import *
from andrei.models import Vehicle
from andrei.logic import *


# Create your views here.

def register_page(request):
    if request.method == 'POST':
        try:
            register_user(request)
            return redirect('main')
        except InvalidCridentialsException as e:
            messages.error(request, e)
            return redirect('main')
    return render(request, 'register_page.html', {})

def login_page(request):
    if request.method == 'POST':
        try:
            login_user(request)
            return redirect('main')
        except InvalidCridentialsException as e:
            messages.error(request, e)
            return redirect('main')
    return render(request, 'login_page.html', {})


def main_page(request):
    context = {}
    return render(request, 'main_page.html', context)

def about_vehicle_page(request, id: str):
    vehicle = Vehicle.objects.get(id=id)
    like_vehicle_class = get_user_like_vehicle_class(request, vehicle)
    context = {
        "vehicle": vehicle,
        'images_set': vehicle.additionalimage_set.all(),
        'like_vehicle_class': like_vehicle_class
    }
    return render(request, 'about_page.html', context=context)

def reviews_page(request):
    return render(request, 'reviews_page.html', {})

def choose_type_page(request):
    return render(request, 'choose_v_type.html', {})

def account_page(request):
    context = {'liked_vehicles': get_liked_vehicles_for_user(request)}
    if request.method == 'POST':
        if request.POST.get('action') == 'Cancel':
            return redirect('account')
        if request.POST.get('action') == 'Signout':
            return redirect('main')
    return render(request, 'account_page.html', context)

def catalog_page(request, category: str):
    vehicles = Vehicle.objects.filter(vtype=category.lower())
    return render(request, 'catalog_page.html', {'vehicles': vehicles})

def add_vehicle_page(request):
    if not user_can_add_vehicle(request.user):
        return redirect('main')

    if request.method == 'POST':
        try:
            add_vehicle(request)
        except UCantAddVehicle as e:
            messages.error(request, e)
        return redirect('main')
    return render(request, 'add_vehicle_page.html', {})

def edit_vehicle_page(request, vehicle_id):
    if not user_can_add_vehicle(request.user):
        return redirect('main')
    
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
    except ObjectDoesNotExist as e:
        return redirect('add_vehicle')

    if request.method == 'POST':
        try:
            edit_vehicle(request, vehicle)
        except UCantAddVehicle as e:
            messages.error(request, e)
        return redirect('main')
    return render(request, 'add_vehicle_page.html', {'vehicle': vehicle})

def delete_vehicle_page(request, vehicle_id):

    if not user_can_add_vehicle(request.user):
        return redirect('main')
    
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
    except ObjectDoesNotExist as e:
        return redirect('main')
    
    if request.method == "POST":
        vehicle.delete()
        return redirect('main')
    
    context = {
        'vehicle_name': vehicle.name,
        'vehicle_id': vehicle.id
    }

    return render(request, 'delete_confirm.html', context=context)

def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect('main')

def like_car_ajax(request):
    if request.user.is_authenticated:
        toggle_like(request.user, Vehicle.objects.get(id=request.POST.get('vehicle_id')))
    return JsonResponse({"status": "Success"})
