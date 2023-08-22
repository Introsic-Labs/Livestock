from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # add additional fields in here
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.username
