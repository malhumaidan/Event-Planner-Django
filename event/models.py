from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


    
class Event(models.Model):
   title= models.CharField(max_length=150)
   image= models.ImageField(blank=True)
   organizer= models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
   number_of_seats= models.IntegerField()
   date_of_event= models.DateField()
   location= models.TextField()
   
   @property
   def remaining_seats(self):
      objects = self.booking_event.all()
      x=0
      for obj in objects:
         x += obj.number_of_booked_seats
      return self.number_of_seats - x


   def __str__(self):
      return self.title

class Booking(models.Model):
   booker= models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
   event= models.ForeignKey(Event, on_delete=models.CASCADE, related_name="booking_event")
   number_of_booked_seats= models.PositiveIntegerField()

   def __str__(self):
      return f"{self.event.title}, by {self.booker}"
