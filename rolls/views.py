from django.shortcuts import render, get_object_or_404
from .models import Roll

# Create your views here.
def rolls(request):
    rolls = Roll.objects.all()
    return render(request, 'rolls/test_django_sushi.html', {'rolls':rolls})

def contacts(resquest):
    return render(resquest, 'rolls/test_contacts.html')

def orders(request):
    rolls = Roll.objects.all()
    return render(request, 'rolls/order.html', {'rolls':rolls})

def orders_show(request, pk):
    rolls = get_object_or_404(Roll, pk=pk)
    return render(request, 'rolls/order_show.html', {'rolls':rolls})