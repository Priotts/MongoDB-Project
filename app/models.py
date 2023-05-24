from userprofile.models import UserProfile
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Order(models.Model):
    ORDER_CHOICES = (
    ('buy', 'Buy'),
    ('sell', 'Sell'),
    )

    ORDER_STATUS = (
    ('open', 'Open'),
    ('closed', 'Closed'),
    )

    profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    quantity = models.FloatField()
    price = models.FloatField()
    order_type = models.CharField(max_length=4, choices=ORDER_CHOICES)
    order_status = models.CharField(max_length=6, choices=ORDER_STATUS, default='open')

    def __str__(self):
        return self.profile.user.username