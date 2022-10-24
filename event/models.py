from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#class Organizer(models.Model):
   # user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class Event(models.Model):
   title= models.CharField(max_length=150)
   image= models.TextField()
   organizer= User.id
   number_of_seats= models.IntegerField()
   # number_of_booked_seats= 
   date_of_event= models.DateField()

   def __str__(self):
      return self.title


   
