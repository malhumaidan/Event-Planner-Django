from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


    
class Event(models.Model):
   title= models.CharField(max_length=150)
   image= models.TextField()
   organizer= models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
   number_of_seats= models.IntegerField()
   date_of_event= models.DateField()
   # number_of_seats=
   # location= models.TextField()

   @property
   def booked(self):
      pass

   def __str__(self):
      return self.title

class Bookings(models.Model):
   booker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
   event= models.OneToOneField(Event, on_delete=models.CASCADE, primary_key=True)

   
