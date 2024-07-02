from django.db import models
from django.utils import timezone

# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=100)
    email= models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name + self.email 

