from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth import logout
from django.http import JsonResponse

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

def about_vehicle_page(request):  #def about_vehicle_page(request, id):
    # vehicle = Vehicle.objects.get(id=id)
    # context = {
    #     "vehicle": vehicle
    # }
    # if request.method == "POST":
    #     toggle_like(request)
    return render(request, 'about_page.html', {'like_vehicle_class':'like-vehicle-pressed'})

def reviews_page(request):
    return render(request, 'reviews_page.html', {})

def choose_type_page(request):
    return render(request, 'choose_v_type.html', {})

def account_page(request):
    return render(request, 'account_page.html', {})

def catalog_page(request):
    return render(request, 'catalog_page.html', {})

def add_vehicle_page(request):
    try:
        add_vehicle(request)
    except UCantAddVehicle as e:
        messages.error(request, e)
        return redirect('main')
    return render(request, 'add_vehicle_page.html', {})

def signup_redirect(request):
    messages.error(request, "Something wrong here, it may be that you already have account!")
    return redirect('main')

def toggle_like(request):
    return render(request)

    # request.user for user *