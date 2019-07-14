from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Catagory(models.Model):
    title = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Expenses(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    rupees = models.FloatField()
    catagory = models.ForeignKey(Catagory,  on_delete=models.CASCADE, default=1)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title