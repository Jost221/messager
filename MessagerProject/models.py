from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()

class Сorrespondence(models.Model):
    name = models.TextField()
    users = models.TextField()

class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correspondence = models.ForeignKey(Сorrespondence, on_delete=models.CASCADE)
