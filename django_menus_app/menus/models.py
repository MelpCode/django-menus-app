from django.db import models

# Create your models here.
class Menus(models.Model):
  starter = models.CharField(max_length=40)
  main = models.CharField(max_length=40)
  dessert = models.CharField(max_length=40)
  price = models.FloatField()
