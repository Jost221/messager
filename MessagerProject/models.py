from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

class Сorrespondence(models.Model):
    id = models.IntegerField(primary_key=True)
    users = models.TextField()

class message(models.Model):
    id = models.IntegerField(primary_key=True)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correspondence = models.ForeignKey(Сorrespondence, on_delete=models.CASCADE)
