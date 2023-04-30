from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

# Create your models here.
class Client (models.Model):
    nom = models.CharField( max_length=50)
    prenom = models.CharField(max_length=100)
    addresse = models.CharField(max_length=100)
    nomUtisateur = models.CharField(max_length=50, default='user', unique=True)
    email = models.EmailField(max_length=254, default='example@example.com')
    telephone = PhoneNumberField(default='+22661748597')
    cnib = models.IntegerField()
    motDePass = models.CharField(max_length=50, default='1234')
    
    

    def __str__(self):
        return self.nom +' '+ self.prenom

class Car(models.Model):
    nom = models.CharField(max_length=50)
    nombre_de_places = models.IntegerField()
    capacite_bagage = models.IntegerField()
    nombre_de_car = models.IntegerField()

    def __str__(self):
        return self.nom
    
    

class Voyage_programmer(models.Model):
    ville_depart = models.CharField(max_length=200)
    ville_arrive = models.CharField(max_length=200)
    heure_depart = models.TimeField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    prix = models.IntegerField()

    def __str__(self):
        return self.ville_depart + ' - '+ self.ville_arrive




class Voyages(models.Model):
    ville_depart = models.CharField(max_length=200)
    ville_arrive = models.CharField(max_length=200)
    heure_depart = models.TimeField()
    place_number = models.IntegerField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    prix = models.IntegerField()

    def __str__(self):
        return self.ville_depart + ' - ' + self.ville_arrive


   
class Reservation(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    voyage = models.ForeignKey(Voyages,on_delete=models.CASCADE)
    NomEtPrenom = models.CharField(max_length=100, default="user")
    date = models.DateField(auto_now=False, auto_now_add=False,)
    valider_reservation = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ['valider_reservation','-date']
        
    
    def __str__(self):
        return str(self.client) + ' - ' + str(self.voyage)
 
    
class Place(models.Model):
    voyage = models.ForeignKey(Voyages, on_delete=models.CASCADE)
    date = models.DateField()
    nombre_de_place_restant = models.IntegerField(default=2)
    disponibilite = models.BooleanField(default=True)

   
    def __str__(self):
        return str(self.date)+ ' - '+str(self.nombre_de_place_restant) + '  Nombre de places restant '
  
  

class Ville(models.Model):
    nom = models.CharField( max_length=50)
    
    
    def __str__(self):
        return self.nom


class Reserve(models.Model):
    NomEtPrenom = models.CharField(max_length=100, default="user")
    villeDepart = models.CharField( max_length=50)
    villeArrive = models.CharField(max_length=50)
    nombreDePlace = models.IntegerField()
    typeVoyage = models.CharField(max_length=50)
    dateReservation= models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.villeDepart + ' - ' + self.villeArrive



  
@receiver(post_save, sender=Reservation)
def misAjourPlace(sender, instance,**kwargs):
    voyageInstanceR = instance.voyage
    reservationDate = instance.date
    try:
        voyageInstanceP = Place.objects.get(voyage = voyageInstanceR, date = reservationDate)
   
        if voyageInstanceP:
            voyageInstanceP.nombre_de_place_restant -= 1
            voyageInstanceP.save()
            if voyageInstanceP.nombre_de_place_restant ==0:
                voyageInstanceP.disponibilite = False
                voyageInstanceP.save()
    except:        
        a = Place.objects.create(voyage = voyageInstanceR, date = reservationDate)
        a.nombre_de_place_restant -=1
        a.save()
        
     
@receiver(post_delete, sender=Reservation)
def reMisAjourPlace(sender, instance, **kwargs):
    voyageInstanceR = instance.voyage
    reservationDate = instance.date
    voyageInstanceP = Place.objects.get(voyage = voyageInstanceR, date = reservationDate)
    voyageInstanceP.nombre_de_place_restant += 1
    voyageInstanceP.save()



class Courier(models.Model):
    nomEtPrenomDeExpediteur = models.CharField(max_length=50)
    nomEtPrenomDuDestinatair = models.CharField(max_length=100)
    objetAEnvoyer = models.CharField( max_length=50)
    prixDeLobjet = models.IntegerField()
    telephone = models.CharField( max_length=50)
    cnib = models.IntegerField()
    validerArrive = models.BooleanField(default=False)
    validerPris = models.BooleanField(default=False)
    
    class Meta:
        ordering=['validerArrive','validerPris']

   
    def __str__(self):
        return self.nomEtPrenomDeExpediteur +'-'+self.nomEtPrenomDuDestinatair
    

    

class UtlisateurConnecter(models.Model):
    identifiant = models.IntegerField()



    
