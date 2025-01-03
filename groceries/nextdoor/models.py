from django.shortcuts import render
from django.db import models
class User(models.Model):
    mobile_number = models.CharField(max_length=15, unique=True)
    otp = models.CharField(max_length=6, blank=True, null=True)
    user_type = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email



        





