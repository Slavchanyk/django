from django.db import models

# Create your models here.
class Users(models.Model):
  FirstName = models.CharField(max_length=255)
  LastName = models.CharField(max_length=255)
  BirthDate = models.DateField()
  RegistrationDate = models.DateField()


class Orders(models.Model):
  CreadedDate = models.DateField()
  Goods = models.CharField(max_length=255)
  User = models.OneToOneField(
    Users,
    on_delete=models.CASCADE,
    primary_key=True,
  )