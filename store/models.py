from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100,null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits= 6,decimal_places=2,null=False, blank=False)
    inventory = models.PositiveSmallIntegerField()
    last_updated = models.DateTimeField(auto_now=True)

class Collection(models.Model):
    title = models.CharField(max_length=100,null=False, blank=False)