from django.db import models

class Vladenie(models.Model):
    adress=models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    vladelec=models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name