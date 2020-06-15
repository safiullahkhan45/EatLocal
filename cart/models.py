from django.db import models
from menu.models import Menu
from users.models import Profile
# Create your models here.

class CartItem(models.Model):
    item = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True, blank=True)
    time_desired = models.DateTimeField(auto_now=False, blank=True, null=True)

    def __str__(self):
        return str(self.item.dish)


class Cart(models.Model):
    meals = models.ManyToManyField(CartItem, blank=True)
    ref_name = models.CharField(max_length=100, default='Empty')
    profile = models.OneToOneField(Profile, on_delete=models.SET_NULL, blank=True, null=True)
    total = models.IntegerField(default=0)
    date_start = models.DateField(auto_now=True)
    date_end = models.DateField(auto_now=True)
    deliver = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ref_name)


