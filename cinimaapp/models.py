from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.CharField(max_length=35)
    desc=models.TextField()
    year=models.IntegerField()
    image=models.ImageField(upload_to='movies/images',blank=True,null=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    phonenumber=models.IntegerField(default=0)
    address=models.TextField(default="")

    def __str__(self):
        return self.username
