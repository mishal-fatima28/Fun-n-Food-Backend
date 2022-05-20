from django.db import models

# Create your models here.

class Timing(models.Model):
	park_Id = models.IntegerField(primary_key=True)
	monday_to_friday = models.CharField(max_length=70) 
	weekend_and_holidays = models.CharField(max_length=70)


class Ticket(models.Model):
	park_Id = models.IntegerField(primary_key=True)
	child_under_33i = models.CharField(max_length=70) 
	child_between_33i_to_4f_6i = models.CharField(max_length=70)
	child_above_4f_6i = models.CharField(max_length=70)
	stag = models.CharField(max_length=70) 
