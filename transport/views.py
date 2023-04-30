from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Client, Car, Voyages, Reservation, Place, Reserve, Ville, Courier
from django.db.models import Q
from .forms import ClientForm, CarForm, VoyagesForm, ReservationForm, CourierForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .serializers import ReserveSerializer, VoyagesSerializer, VilleSerializer, ClientSerializer, CourierSerializer
from rest_framework import  generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

ide = 0
@api_view(['POST'])
def verifeLogin(request):
        data = json.loads(request.body)
        userName = data.get('nomUtisateur')
        mdp = data.get('motDePass')
        a = Client.objects.get(nomUtisateur=userName)
        global ide
        ide = a.id
        try:

            if a.motDePass == mdp:
                response_data = {'success': True, 'message': 'Modèle enregistré avec succès.'}
                return JsonResponse(response_data, status=201)
        except:
            print(userName)
            print(mdp)
            print(a.nom)
            response_data = {'success': True, 'message': 'Modèle enregistré avec succès.'}
            return JsonResponse(response_data, status = 400)


@api_view(['POST'])
def createClient(request):
    serializer = ClientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('YES')
        return Response(serializer.data, status=201)
    print('NON')
    print(serializer.errors)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def createCourier(request):
    serializer = CourierSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('YES')
        return Response(serializer.data, status=201)
    print('NON')
    print(serializer.errors)
    return Response(serializer.errors, status=400)
class VoyageList(generics.ListAPIView):
    queryset = Voyages.objects.all()
    serializer_class = VoyagesSerializer

@api_view(['POST'])
def createReserve(request):
    serializer = ReserveSerializer(data=request.data)
    if serializer.is_valid():
        donnees = request.data
        
        serializer.save()
        print('YES')
        
        villeDepar = donnees.get('villeDepart')
        villeArriv = donnees.get('villeArrive')
        print(villeDepar + ' '+villeArriv)
        dateReservation=donnees.get('dateReservation')
        voyage = Voyages.objects.get(ville_depart=villeDepar, ville_arrive=villeArriv)
        print(ide)
        client = Client.objects.get(id=ide)
        reservat = Reservation.objects.create(client=client, voyage=voyage, date=dateReservation)
        reservat.save()
        return Response(serializer.data, status=201)
    print('NON')
    print(serializer.errors)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def createReservePourUnePersonne(request):
    serializer = ReserveSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        print('YES')
        donnees = request.data
        villeDepar = donnees.get('villeDepart')
        villeArriv = donnees.get('villeArrive')
        nomEtPrenom = donnees.get('NomEtPrenom')
        print(villeDepar + ' '+villeArriv)
        dateReservation=donnees.get('dateReservation')
        voyage = Voyages.objects.get(ville_depart=villeArriv, ville_arrive=villeDepar)
        print(ide)
        client = Client.objects.get(id=ide)
        reservat = Reservation.objects.create(client=client, voyage=voyage, 
                                              date=dateReservation, 
                                              NomEtPrenom=nomEtPrenom)
        reservat.save()
        return Response(serializer.data, status=201)
    print('NON')
    print(serializer.errors)
    return Response(serializer.errors, status=400)

class ClientEnregistre(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field ='id'
    
class VilleList(generics.ListAPIView):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer

def profile(request):
    return redirect('profile', ide)

@login_required
def home(request):
    clientcount = Client.objects.count()
    couriercount = Courier.objects.filter(Q(validerArrive=False)| Q(validerPris=False)).count()
    couriertotal = Courier.objects.all().count()
    courierArriver = Courier.objects.filter(validerArrive = True).count()
    courierPris = Courier.objects.filter(validerPris=True).count()
    Voyagescount = Voyages.objects.count()
    reservationcount = Reservation.objects.filter(valider_reservation=False).count()
    reservationtotal = Reservation.objects.all().count()


    return render(request, 'admin_t/homeAdmin.html',{
                    'nombreClient': clientcount, 'nombreCourier': couriercount,
                    'nombreVoyages': Voyagescount, 'nombreReservation': reservationcount,
                    'couriertotal':couriertotal, 'courierArriver':courierArriver,
                    'courierPris':courierPris, 'reservationtotal':reservationtotal,
                    
                    }
                  )


@login_required
def client(request, id=0):

    if 'editClient' in request.path and id != 0 :

        model = get_object_or_404(Client, pk=id)
        if request.method == 'POST':
            form = ClientForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('client')
            else:
                form = ClientForm(instance=model)
                return render(request, 'admin_t/client.html', {"form": form})
        form = ClientForm(instance=model)
        return render(request, 'admin_t/client.html', {"form": form, 'id':id})

    elif 'deleteClient' in request.path and id != 0:
        ob = get_object_or_404(Client, id=id)
        ob.delete()
        return redirect('client')

    else:


        if request.method == "POST" and 'addClient' in request.path:
            form = ClientForm(request.POST)
            visit = Client.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            client = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "Client added !")
                return redirect('client')
            else:
                return render(request, 'admin_t/client.html', {"form": form, "models":client})
        else:
            form = ClientForm()
            visit = Client.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            client = page.get_page(pge)
            return render(request, 'admin_t/client.html', {"form": form, "models":client})


@login_required
def courier(request, id=0):

    if 'editCourier' in request.path and id != 0 :

        model = get_object_or_404(Courier, pk=id)
        if request.method == 'POST':
            form = CourierForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('courier')
            else:
                form = CourierForm(instance=model)
                return render(request, 'admin_t/courier.html', {"form": form})
        form = CourierForm(instance=model)
        return render(request, 'admin_t/courier.html', {"form": form, 'id':id})

    elif 'deleteCourier' in request.path and id != 0:
        ob = get_object_or_404(Courier, id=id)
        ob.delete()
        return redirect('courier')

    else:


        if request.method == "POST" and 'addCourier' in request.path:
            form = CourierForm(request.POST)
            visit = Courier.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            courier = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "Courier added !")
                return redirect('courier')
            else:
                return render(request, 'admin_t/courier.html', {"form": form, "models":courier})
        else:
            form = CourierForm()
            visit = Courier.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            courier = page.get_page(pge)
            return render(request, 'admin_t/courier.html', {"form": form, "models":courier})



@login_required
def car(request, id=0):

    if 'editCar' in request.path and id != 0 :

        model = get_object_or_404(Car, pk=id)
        if request.method == 'POST':
            form = CarForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('car')
            else:
                form = CarForm(instance=model)
                return render(request, 'admin_t/car.html', {"form": form})
        form = CarForm(instance=model)
        return render(request, 'admin_t/car.html', {"form": form, 'id':id})

    elif 'deleteCar' in request.path and id != 0:
        ob = get_object_or_404(Car, id=id)
        ob.delete()
        return redirect('car')

    else:


        if request.method == "POST" and 'addCar' in request.path:
            form = CarForm(request.POST)
            visit = Car.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            car = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "car added !")
                return redirect('car')
            else:
                return render(request, 'admin_t/car.html', {"form": form, "models":car})
        else:
            form = CarForm()
            visit = Car.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            car = page.get_page(pge)
            return render(request, 'admin_t/car.html', {"form": form, "models":car})
        
def validerReservation(request, id):
    valider = get_object_or_404(Reservation, id=id)
    valider.valider_reservation = True
    valider.save()
    return redirect('reservation')


def validerCourier(request, id):
    courier = get_object_or_404(Courier, id=id)
    if 'Arrive' in request.path:
        courier.validerArrive = True
    elif 'Pris' in request.path:
        courier.validerPris = True
    courier.save()
    return redirect('courier')
        
@login_required
def voyage(request, id=0):

    if 'editVoyage' in request.path and id != 0 :

        model = get_object_or_404(Voyages, pk=id)
        if request.method == 'POST':
            form = VoyagesForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('voyage')
            else:
                form = VoyagesForm(instance=model)
                return render(request, 'admin_t/voyage.html', {"form": form})
        form = VoyagesForm(instance=model)
        return render(request, 'admin_t/voyage.html', {"form": form, 'id':id})

    elif 'deleteVoyage' in request.path and id != 0:
        ob = get_object_or_404(Voyages, id=id)
        ob.delete()
        return redirect('voyage')

    else:


        if request.method == "POST" and 'addVoyage' in request.path:
            form = VoyagesForm(request.POST)
            visit = Voyages.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            voyage = page.get_page(pge)
            if form.is_valid():
                form.save()
                messages.success(request, "voyage added !")
                return redirect('voyage')
            else:
                return render(request, 'admin_t/voyage.html', {"form": form, "models":voyage})
        else:
            form = VoyagesForm()
            visit = Voyages.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            voyage = page.get_page(pge)
            return render(request, 'admin_t/voyage.html', {"form": form, "models":voyage})

@login_required
def reservation(request, id=0):

    if 'editReservation' in request.path and id != 0 :

        model = get_object_or_404(Reservation, pk=id)
        if request.method == 'POST':
            form = ReservationForm(request.POST, instance=model)
            if form.is_valid():
                form.save()
                return redirect('reservation')
            else:
                form = ReservationForm(instance=model)
                return render(request, 'admin_t/reservation.html', {"form": form})
        form = ReservationForm(instance=model)
        return render(request, 'admin_t/reservation.html', {"form": form, 'id':id})

    elif 'deleteReservation' in request.path and id != 0:
        ob = get_object_or_404(Reservation, pk=id)
        ob.delete()
        return redirect('reservation')

    else:


        if request.method == "POST" and 'addReservation' in request.path:

            form = ReservationForm(request.POST)
            visit = Reservation.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            reservation = page.get_page(pge)
            if form.is_valid():

                try:
                    b = form.cleaned_data['date']
                    a = Place.objects.get(date=b)
                    if a.disponibilite:
                        form.save()
                        messages.success(request, "Reservation added !")
                        return redirect('reservation')
                    else:
                        return HttpResponse("Vous ne pouvez plus reserver car il n'y a plus de place disponibles a cette date")
                except:
                    form.save()
                    messages.success(request, "Reservation added !")
                    return redirect('reservation')
            else:
                return render(request, 'admin_t/reservation.html', {"form": form, "models":reservation})
        else:
            form = ReservationForm()
            visit = Reservation.objects.all()
            page = Paginator(visit, 5)
            pge = request.GET.get('page')
            reservation = page.get_page(pge)
            return render(request, 'admin_t/reservation.html', {"form": form, "models":reservation})


