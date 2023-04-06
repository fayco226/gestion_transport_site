from django.contrib import admin
from .models import Car, Client, Voyages, Voyage_programmer, Reservation, Place, Reserve, Ville
# Register your models here.
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Voyage_programmer)
admin.site.register(Voyages)
admin.site.register(Reservation)
admin.site.register(Place)
admin.site.register(Reserve)
admin.site.register(Ville)