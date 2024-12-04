
from django.db import models

class Books(models.Model):
    name=models.CharField(max_length=255)
    price=models.FloatField()
    stock=models.IntegerField()
    image=models.CharField(max_length=2083)

    def __str__(self):
        return self.name


