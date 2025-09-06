from django.db import models

# Create your models here.
class Roll(models.Model):
    img = models.ImageField()
    name = models.CharField(max_length=30)
    price = models.FloatField()
    
    def __str__(self):
        return self.name
    