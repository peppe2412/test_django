from django.db import models

# Create your models here.
class Roll(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=30)
    price = models.FloatField()
    description = models.CharField(default='no descrizione')
    
    def __str__(self):
        return self.name
    