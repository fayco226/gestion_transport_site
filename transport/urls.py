from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home/', views.home, name="home"),

    path('client/',views.client, name="client"),
    path('addClient', views.client, name="addClient"),
    path("editClient/<id>/", views.client, name="editClient"),
    path("deleteClient/<id>/", views.client, name="deleteClient"),

    path('voyage/', views.voyage, name='voyage'),
    path('voyage/detail/<id>',views.voyage, name='voyageid' ),
    path('addVoyage/', views.voyage, name='addVoyage' ),
    path("editVoyage/<id>", views.voyage, name="editVoyage"),
    path("deleteVoyage/<id>/", views.voyage, name="deleteVoyage"),

    path('car/', views.car, name="car"),
    path('addCar/', views.car, name="addCar"),
    path("editCar/<id>", views.car, name="editCar"),
    path("deleteCar/<id>/", views.car, name="deleteCar"),

    path('reservation/', views.reservation, name="reservation"),
    path('addReservation/', views.reservation, name="addReservation"),
    path("editReservation/<id>", views.reservation, name="editReservation"),
    path("deleteReservation/<id>/", views.reservation, name="deleteReservation"),
    path('validerReservation/<id>', views.validerReservation, name='validerReservation'),
    

    path('courier/', views.courier, name="courier"),
    path('addCourier/', views.courier, name="addCourier"),
    path("editCourier/<id>", views.courier, name="editCourier"),
    path("deleteCourier/<id>/", views.courier, name="deleteCourier"),
    path('validerArrive/<id>', views.validerCourier, name='validerArrive'),
    path('validerPris/<id>', views.validerCourier, name="validerPris"),


     path('api/voyages/', views.VoyageList.as_view()),
     path('reservations/create/', views.createReserve, name='reservation-create'),
     path('reservations/create/personne', views.createReservePourUnePersonne, name='reserver_personne'),
     path('client/enregistrement/', views.createClient, name = 'enregistreClient'),
     path('api/ville/', views.VilleList.as_view(), name='ville'),
     path('api/VerifeLogin', views.verifeLogin, name='VerifeLogin'),
     path('api/courier/', views.createCourier, name='courierApi'),
     path('api/client/<int:id>/', views.ClientEnregistre.as_view(), name='profile'),
     path('api/profile', views.profile, name='profil')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)