from django.db import models

# Create your models here.
class expance(models.Model):
	expance_name = models.CharField(max_length=20)
	expance_amount = models.IntegerField()

class initial_balance(models.Model):
	initial_bal=models.IntegerField()

