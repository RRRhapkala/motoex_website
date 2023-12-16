# Register your models here.
from django.contrib import admin
from andrei.models import Vehicle, MainImage, AdditionalImage

admin.site.register(Vehicle)
admin.site.register(MainImage)
admin.site.register(AdditionalImage)