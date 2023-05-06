from django.db import models

# Create your tests here.
class User(models.Model):
  username = models.CharField(max_length=60)
  email = models.EmailField(max_length=60)
  password = models.CharField(max_length=255)
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)