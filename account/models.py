from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User)
    btc = models.PositiveIntegerField(default=0, verbose_name="BitCoin")
    msc = models.PositiveIntegerField(default=0, verbose_name="maidsafecoin")
    eth = models.PositiveIntegerField(default=0, verbose_name="Ethereum")
    lit = models.PositiveIntegerField(default=0, verbose_name="Litecoin")
    dol = models.PositiveIntegerField(default=0, verbose_name="Dollor")
    ass = models.PositiveIntegerField(default=0, verbose_name="Asset")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
