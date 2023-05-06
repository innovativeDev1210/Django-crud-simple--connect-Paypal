from django.db import models

# Create your tests here.
class Transaction(models.Model):
    send_user = models.CharField(max_length=60)
    receive_user = models.CharField(max_length=60)
    state = models.BooleanField(default=False)
    amount = models.FloatField()
    monetary_unit = models.CharField(max_length=60)
    created_at = models.DateTimeField()
    allow = models.BooleanField(default=False)