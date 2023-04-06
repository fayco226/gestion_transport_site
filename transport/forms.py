from .models import Client, Car, Voyages, Reservation
from django.forms import ModelForm

class ClientForm(ModelForm):
    
    class Meta:
        model = Client
        fields = '__all__' 
        
class CarForm(ModelForm):
    
    class Meta:
        model = Car
        fields = '__all__'
        
class VoyagesForm(ModelForm):
    
    class Meta:
        model = Voyages
        fields = '__all__'
        
class ReservationForm(ModelForm):
    
    class Meta:
        model = Reservation
        fields = '__all__'


