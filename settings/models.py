from django.db import models
from django.contrib.auth.models import User

from display.models import Member

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    member = models.ForeignKey('display.Member', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.user}"