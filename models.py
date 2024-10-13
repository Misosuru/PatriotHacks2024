#https://www.geeksforgeeks.org/how-to-connect-django-with-reactjs/

from django.db import models

# Create your models here.


class React(models.Model):
    name = models.CharField(max_length=30)
    detail = models.CharField(max_length=500)
