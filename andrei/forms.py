from django.forms import ModelForm
from andrei.models import Vehicle

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'name',
            'description',
            'lon',
            'lat',
            '_type',
            'engine',
            'fuel_type',
            'transmission',
            'year_of_prod',
            'mileage',
            'hometown',
            'currently_in'
        ]