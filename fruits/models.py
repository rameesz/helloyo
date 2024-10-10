
# Create your models here.
# fruits/models.py
from django.db import models

class FruitSet(models.Model):
    fruit1 = models.CharField(max_length=50)
    fruit2 = models.CharField(max_length=50)
    fruit3 = models.CharField(max_length=50)
    fruit4 = models.CharField(max_length=50)
    fruit5 = models.CharField(max_length=50)
    result = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fruit1}, {self.fruit2}, {self.fruit3}, {self.fruit4}, {self.fruit5} - {self.result}"
