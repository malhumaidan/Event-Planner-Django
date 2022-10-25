from django.shortcuts import redirect, render
from .forms import Registration, UserLogin, EventForm
from django.contrib.auth import login, authenticate, logout
from .models import Event

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

def add_event(req):
    form = EventForm()
    if req.method == "POST":
        form = EventForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("home_page")

    context = {
        "form": form
    }

    return render(req,"add-event.html" , context)

def get_events(req):

    events = Event.objects.all()
    events_list= []

    for event in events:
        events_list.append(
            {
                "id":event.id,
                "title": event.title,
                "image": event.image,
                "number_of_seats": event.number_of_seats,
                "date_of_event": event.date_of_event,
                   
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
            
        }
    }
    return render(req, "event-details.html", context)



