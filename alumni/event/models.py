from django.db import models
from django.contrib.auth.models import User as AuthUser

# Create your models here.

gender = (
	('m','male'),
	('f','female'),
	)



class User(models.Model):
	user=models.ForeignKey(AuthUser,on_delete=models.CASCADE)
	name = models.CharField(max_length=20)
	gender = models.CharField(max_length=7,choices=gender)
	branch = models.CharField(max_length=15)
	paasout_year = models.DateField()
	dob = models.DateField()
	address = models.CharField(max_length=50)
	contact_number = models.CharField(max_length=15)
	is_admin = models.BooleanField()



	def __str__(self):
		return self.name




class Event(models.Model):
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=100)
	venue = models.CharField(max_length=50)
	schedule = models.DateField()


	def __str__(self):
		return self.title