from django.shortcuts import render
from .models import Roll

# Create your views here.
def rolls(request):
    rolls = Roll.objects.all()
    return render(request, 'rolls/test_django_sushi.html', {'rolls':rolls})

def contacts(resquest):
    return render(resquest, 'rolls/test_contacts.html')