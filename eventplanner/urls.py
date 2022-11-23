"""eventplanner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from event import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.landing_page, name="empty"),
    path('admin/', admin.site.urls, name="admin_page"),
    path('home/', views.get_events, name="home_page"),
    path('register/', views.user_register, name="register"),
    path('login/', views.user_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('add/event/', views.add_event, name="add_event"),
    path('event/details/<int:event_id>/', views.get_details, name="event_details"),
    path('profile/<int:user_id>/', views.edit_profile, name="edit-profile"),
    path('booking/<int:event_id>/', views.book_seats, name="booking_event"),
    path('org/<int:user_id>/', views.get_org_events, name="org_events"),
    path('follow/<int:user_id>/', views.follow, name="follow"),
    path('dashboard/<int:user_id>/', views.dashboard, name="dashboard"),
    path('results/', views.search, name="search"),
    # path('booking/full/', views.full_event, name="full-page"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)