from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User
from datetime import datetime    
from django.core.validators import MinLengthValidator

class Tank(models.Model):
	# foreign key to the user who owns it
	user = models.ForeignKey(User, default=1)
	# latitude of the Tank
	latitude=models.FloatField(default=0)
	#longitue of the tank
	longitude=models.FloatField(default=0)
	def __str__(self):
		return "Tank "+str(self.id)

class Plant(models.Model):
	# foreign key to the user who owns it
	user = models.ForeignKey(User, default=1)
	# foreign key to tank which waters the plant
	tank=models.ForeignKey(Tank,on_delete=models.CASCADE)
	city=models.CharField(default="Sri City",max_length=100)
	# latitude of the Plant
	latitude=models.FloatField(default=13.5232)
	# longitude of the Plant
	longitude=models.FloatField(default=79.9982)
	# average Soil Moisture of the plant
	averageSoilMoisture=models.FloatField(default=0)
	# average pH of by the plant
	averagepH=models.FloatField(default=0)
	def __str__(self):
		return "Plant "+str(self.id)

class Plant_Data(models.Model):
	# foreign key of the plant 
	plant=models.ForeignKey(Plant,on_delete=models.CASCADE)
	# soil moisture of the plant
	soilMoisture=models.IntegerField(default=0)
	# soil pH of the plant
	pH=models.FloatField(default=0)
	# date and time when it was recorded
	date_time= models.DateTimeField(default=datetime.now, blank=True)
	# weather it is raining or not
	raining=models.BooleanField(default=False)
	def __str__(self):
		return "Plant_Data "+str(self.id)

class Tank_Data(models.Model):
	# foreign key of the tank
	tank=models.ForeignKey(Tank,on_delete=models.CASCADE)
	# tankWaterLevel of the tank reported
	tankWaterLevel=models.IntegerField(default=0)
	def __str__(self):
		return "Tank_Data "+str(self.id)
