from django.db import models

# Create your tests here.
class Wallet(models.Model):
  user_id = models.CharField(max_length=60)
  balance = models.IntegerField(max_length=60)
  monetary_unit = models.CharField(max_length=60)
