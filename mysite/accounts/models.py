from django.db import models

# Create your models here.


class TUser(models.Model):
    uname = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    following = models.ManyToManyField('self',related_name='followers',symmetrical=False,blank=True)
