from django.db import models


class User(models.Model):
    phone = models.IntegerField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()
    description = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    



