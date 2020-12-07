from django.db import models
from django.utils import timezone
from accounts.models import TUser
# from django.contrib.auth.models import User

# Create your models here.


class tweet(models.Model):
    text = models.CharField(max_length=280, default="")
    datetime = models.DateTimeField(default=timezone.now)
    uname = models.ForeignKey(TUser,on_delete=models.CASCADE)
#   uname = models.ForeignKey(User, on_delete=models.CASCADE)
