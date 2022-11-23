import datetime
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BookingForm, Registration, UserLogin, EventForm
from django.contrib.auth import login, authenticate, logout
from .models import Booking, Event, Relation
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.


def user_register(req):


    form = Registration()
    if req.method == "POST":
        form = Registration(req.POST)
        if form.is_valid():
            user= form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(req, user)

        
            return redirect("home_page")

    context={
        "form": form
    }

    return render(req, "registration.html", context)

def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                return redirect("home_page")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def user_logout(request):
    logout(request)
    return redirect("home_page")

def add_event(request):
    form = EventForm()
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event= form.save(commit=False)

            event.organizer= request.user
            event.save()
            return redirect("home_page")

    context = {
        "form": form
    }

    return render(request,"add-event.html" , context)


def get_events(req):

    current_date = datetime.date.today()

    events = Event.objects.all()
    events_list= []

    for event in events:
        if event.date_of_event >= current_date:
            events_list.append(
                {
                    "id":event.id,
                    "title": event.title,
                    "image": event.image,
                    "number_of_seats": event.number_of_seats,
                    "date_of_event": event.date_of_event,
                    "organizer": event.organizer,
                    "remaining": event.remaining_seats,
                    
                }
            )
        
            
    context = {
        "events": events_list
    }

    return render(req, "home-page.html", context)

def get_details(req, event_id):
    event = Event.objects.get(id=event_id)

    

    context = {
        "event": {
            "id":event.id,
            "title": event.title,
            "image": event.image,
            "date_of_event": event.date_of_event,
            "number_of_seats": f"Total seats: {event.number_of_seats}",
            "remaining": f"Remaining seats: {event.remaining_seats}",
        }
    }

    return render(req, "event-details.html", context)

def edit_profile(req, user_id):
    user = User.objects.get(id=user_id)
    events = user.events.all()

    form = Registration(instance=req.user)
    if req.method == "POST":
        form = Registration(req.POST, instance=req.user)
        if form.is_valid():
            user= form.save()
            login(req, user)
            return redirect("home_page")

   
    context = {
        "user_id": user_id,
        "events": events,
        "form": form,
    }
    return render(req, 'edit-profile.html', context)

def book_seats(req, event_id):
    event = Event.objects.get(id=event_id)
    form = BookingForm()
    if req.method == "POST":
        form = BookingForm(req.POST)
        if form.is_valid():
            booking= form.save(commit=False)
            booking.booker= req.user
            booking.event= event
            if booking.number_of_booked_seats > event.remaining_seats:
                return HttpResponse("exceeded")
            booking.save()
            return redirect("home_page")
    elif event.number_of_seats <= event.event_full:
        return HttpResponse("event is full!!")

    context = {
        "id":event_id,
        "form": form,
    }

    return render(req, "booking.html", context)

def landing_page(req):
    search_event = req.GET.get('search')
    if search_event:
        events = Event.objects.filter(organizer = search_event)
    else:
    # If not searched, return default posts
        events = Event.objects.all()

    context = {
        "events": events
    }


    return render(req, "landing-page.html", context)
    

def get_org_events(req, user_id):
    
    user = User.objects.get(id=user_id)
    events = user.events.all()
    # This first finds the user then gets the events list
    # events = User.objects.get(id=user_id).events.all()

    # def follow(req):
    #     Relation.objects.create(following=req.user, followers=user)


    context = {
        "user_id": user_id,
        "events": events,
        "user": user,
        # "follow": follow
    }

    return render(req, "org-events.html",context)

def follow(req, user_id):
    user = User.objects.get(id=user_id)
    Relation.objects.create(following=user, follower=req.user)

    context = {
        "user" : user,
    }
    return (req, context)



def dashboard(req, user_id):
    user = User.objects.get(id=user_id)
    events = user.events.all()

    form = EventForm()
    if req.method == "POST":
        form = EventForm(req.POST, req.FILES)
        if form.is_valid():
            event= form.save(commit=False)

            event.organizer= req.user
            event.save()
            redirect("dashboard")


    following_list = Relation.objects.filter(follower=req.user)
    followers_list = Relation.objects.filter(following=req.user)

    context = {
        "user_id": user_id,
        "events": events,
        "form": form,
        "following": following_list,
        "followers": followers_list,
    }

    return render(req, "dashboard.html",context)


def search(req):
    events = Event.objects.all()

    context = {
        "events": events
    }
    return render(req, "search.html", context)

