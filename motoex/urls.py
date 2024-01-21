"""
URL configuration for motoex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from andrei.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page, name='main'),
    path('about/<int:id>/', about_vehicle_page, name='about'),
    path('reviews/', reviews_page, name='reviews'),
    path('choose_vehicle_type/', choose_type_page, name='choose_vehicle'),
    path('account/', account_page, name='account'),
    path('catalog/<str:category>/', catalog_page, name='catalog'),
    path('sign_up/', register_page, name='register'),
    path('sign_in/', login_page, name='login'),
    path('add_vehicle/', add_vehicle_page, name='add_vehicle'),
    path('edit_vehicle/<int:vehicle_id>/', edit_vehicle_page, name='edit_vehicle'),
    path('delete_vehicle/<int:vehicle_id>/', delete_vehicle_page, name='delete_vehicle'),
    path('toggle_like/', like_car_ajax, name='toggle_like'),
    path('', include("allauth.urls")),
    path('social/signup/', signup_redirect, name='signup_redirect'),
    path('accounts/profile/', signup_redirect, name='profile')
]   + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)\
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
