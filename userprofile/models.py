from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    walletbtc = models.FloatField(blank=True)
    usd = models.FloatField(blank=True)
    profit = models.FloatField(default=0, blank=True)
    
    def __str__(self):
        return self.user.username 

