from multiprocessing import Event
from django.contrib import admin
from .models import Event, Booking,Following
# Register your models here.
admin.site.register(Event)
admin.site.register(Booking)
admin.site.register(Following)