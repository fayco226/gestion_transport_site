from rest_framework import serializers
from .models import Reservation, Client, Voyages, Ville, Reserve, Courier

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class VoyagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voyages
        fields = ('ville_depart', 'ville_arrive', 'heure_depart', 'prix', )

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = '__all__'

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserve
        fields = '__all__'
class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'