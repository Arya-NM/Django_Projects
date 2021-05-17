from django.db import models

# Create your models here.
class contact(models.Model):
	name = models.CharField(max_length=20)
	phone_number = models.IntegerField()


