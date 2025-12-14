from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    role=models.CharField(null=True)
    otp=models.CharField(null=True)
    is_verified=models.BooleanField(default=False)


