from django.urls import path
from . import views

urlpatterns = [
    path('', views.rolls, name='home'),
    path('contact', views.contacts, name='contact'),
    path('order', views.orders, name='order'),
    path('order/<int:pk>', views.orders_show, name='order-show')
]