# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.
from datetime import datetime    

class Tank(models.Model):
	user = models.ForeignKey(User, default=1)
	latitude=models.FloatField(default=0)
	longitude=models.FloatField(default=0)
	min_water=models.IntegerField(default=0)
	def __str__(self):
		return "Tank "+str(self.id)

class Plant(models.Model):
	user = models.ForeignKey(User, default=1)
	tank=models.ForeignKey(Tank,on_delete=models.CASCADE)
	latitude=models.FloatField(default=0)
	longitude=models.FloatField(default=0)
	averageSoilMoisture=models.FloatField(default=0)
	averagepH=models.FloatField(default=0)
	idealSoilMoisture=models.IntegerField(default=0)
	idealpH=models.FloatField(default=0)
	def __str__(self):
		return "Plant "+str(self.id)

class Plant_Data(models.Model):
	plantID=models.ForeignKey(Plant,on_delete=models.CASCADE)
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