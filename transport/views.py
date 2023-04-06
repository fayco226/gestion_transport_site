from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Client, Car, Voyages, Reservation, Place, Reserve, Ville
from .forms import ClientForm, CarForm, VoyagesForm, ReservationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework.views import APIView
from .serializers import ReserveSerializer, VoyagesSerializer, VilleSerializer, ClientSerializer, CourierSerializer
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json


@api_view(['POST'])
def verifeLogin(request):
        data = json.loads(request.body)
        userName = data.get('nomUtisateur')
        mdp = data.get('motDePass')
        a = Client.objects.get(nomUtisateur=userName)
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
        serializer.save()
        print('YES')
        return Response(serializer.data, status=201)
    print('NON')
    print(serializer.errors)
    return Response(serializer.errors, status=400)

class ClientEnregistre(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    

    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        if serializer.errors:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)   
class VilleList(generics.ListAPIView):
    queryset = Ville.objects.all()
    serializer_class = VilleSerializer

@login_required
def home(request):
    clientcount = Client.objects.count()
    carcount = Car.objects.count()
    Voyagescount = Voyages.objects.count()
    reservationcount = Reservation.objects.count()
    
    return render(request, 'admin_t/homeAdmin.html', {'nombreClient': clientcount, 'nombreCar': carcount, 'nombreVoyages': Voyagescount, 'nombreReservation': reservationcount, })


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


        