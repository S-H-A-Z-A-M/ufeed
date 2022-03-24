from django.db import models
from django.core.validators import ProhibitNullCharactersValidator


# Create your models here.



class Register(models.Model):
    name = models.CharField(max_length=30 )
    email = models.EmailField()
    password = models.CharField(max_length=30 )
    contact = models.CharField(max_length=17)

    def __str__(self):
        return f"{self.name},{self.email},{self.password},{self.contact}"


class problem(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name},{self.email},{self.subject},{self.message}"

class sign_in(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.email},{self.password}"

class donate(models.Model):
    name= models.CharField(max_length=50)
    contact = models.CharField(max_length=17)
    address = models.CharField(max_length=300)
    amount = models.IntegerField(unique=True, null=True)       