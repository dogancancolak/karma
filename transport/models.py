from django.db import models
import random


class Bus(models.Model):
    plateNumber = models.TextField(max_length=255)
    #details = models.TextField(max_length=255, default="", null=True)
    #garage = models.TextField(max_length=255, default="", null=True)
    type = models.TextField(max_length=255, default="", null=True)

    def getCurrentPosition(self):
        return {'x': 2, 'y': 5}

    def getCurrentDriver(self):
        return "Dummy User"


class Driver(models.Model):
    firstName = models.TextField(max_length=255)
    lastName = models.TextField(max_length=255)
    registrationNumber = models.TextField(max_length=255)


class BusStop(models.Model):
    stopNumber = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
