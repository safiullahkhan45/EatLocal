from django.db import models

# Create your models here.

class Plan(models.Model):
    name = models.CharField(max_length=200, null=True)
    plan_id = models.IntegerField(default=1)
    max_meals = models.IntegerField(default=5)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.IntegerField(default=5)
    image = models.ImageField(upload_to='images/plans', default='default.jpg')

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    opening_year = models.CharField(max_length=4, null=True)
    story = models.TextField(null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, default=1)
    dish = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='images/menu', default='default.jpg')
    description = models.TextField(null=True)

    def __str__(self):
        return self.dish
