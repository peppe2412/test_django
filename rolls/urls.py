from django.urls import path
from . import views

urlpatterns = [
    path('', views.rolls, name='home'),
    path('contact', views.contacts, name='contact')
]