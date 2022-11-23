from email.mime import image
from email.policy import default
from django.db import models
from django.contrib.auth.models import User


    
class Event(models.Model):
   title= models.CharField(max_length=150)
   image= models.ImageField(blank=True, upload_to="media")
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

   @property
   def event_full(self):
      objects = self.booking_event.all()
      reservations = 0
      for x in objects:
         reservations += x.number_of_booked_seats
      return reservations

   def __str__(self):
      return f"{self.title}"

class Booking(models.Model):
   booker= models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
   event= models.ForeignKey(Event, on_delete=models.CASCADE, related_name="booking_event")
   number_of_booked_seats= models.PositiveIntegerField()

   def __str__(self):
      return f"{self.event.title} Booking Details"


class Relation(models.Model):
   following = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
   follower = models.ForeignKey(User, related_name="follower", on_delete=models.CASCADE)

   def __str__(self):
      return f"user: {self.following} / followed by: {self.follower}"
