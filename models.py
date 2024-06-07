from django.db import models

class day(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(default=18)
