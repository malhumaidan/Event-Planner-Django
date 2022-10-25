from email.mime import image
from django.db import models
from django.contrib.auth.models import User


    
class Event(models.Model):
   title= models.CharField(max_length=150)
   image= models.TextField()
   # organizer= models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
   number_of_seats= models.IntegerField()
   date_of_event= models.DateField()
   # location= models.TextField()

   @property
   def booked(self):
      pass

   def __str__(self):
      return self.title


   
