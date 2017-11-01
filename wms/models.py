from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import Permission, User
from datetime import datetime    
from django.core.validators import MinLengthValidator

class UserProfile(models.Model):
	user=models.OneToOneField(User)
	contactno=models.CharField(max_length=10,validators=[MinLengthValidator(10)],blank=True)
	def __str__(self):
		return "%s's profile"%self.user
		
class Tank(models.Model):
	# foreign key to the user who owns it
	user = models.ForeignKey(User, default=1)
	# latitude of the Tank
	latitude=models.FloatField(default=0)
	#longitue of the tank
	longitude=models.FloatField(default=0)
	# min_ water level in the tank
	min_water=models.IntegerField(default=0)
	def __str__(self):
		return "Tank "+str(self.id)

class Plant(models.Model):
	# foreign key to the user who owns it
	user = models.ForeignKey(User, default=1)
	# foreign key to tank which waters the plant
	tank=models.ForeignKey(Tank,on_delete=models.CASCADE)
	# latitude of the Plant
	latitude=models.FloatField(default=0)
	# longitude of the Plant
	longitude=models.FloatField(default=0)
	# average Soil Moisture of the plant
	averageSoilMoisture=models.FloatField(default=0)
	# average pH of by the plant
	averagepH=models.FloatField(default=0)
	# ideal Soil Moisture required bty the plant
	idealSoilMoisture=models.IntegerField(default=0)
	# ideal pH required by the plant
	idealpH=models.FloatField(default=0)
	def __str__(self):
		return "Plant "+str(self.id)

class Plant_Data(models.Model):
	# plant id of the data 
	plantID=models.ForeignKey(Plant,on_delete=models.CASCADE)
	# 
	soilMoisture=models.IntegerField(default=0)
	pH=models.FloatField(default=0)
	date_time= models.DateTimeField(default=datetime.now, blank=True)
	raining=models.BooleanField(default=False)
	def __str__(self):
		return "Plant_Data "+str(self.id)


class Tank_Data(models.Model):
	tankID=models.ForeignKey(Tank,on_delete=models.CASCADE)
	tankWaterLevel=models.IntegerField(default=0)
	def __str__(self):
		return "Tank_Data "+str(self.id)

class Actuator(models.Model):
	user = models.ForeignKey(User, default=1)
	plantID=models.ForeignKey(Plant,on_delete=models.CASCADE)
	water_supplied=models.IntegerField(default=0)
	def __str__(self):
		return "Actuator "+str(self.id)