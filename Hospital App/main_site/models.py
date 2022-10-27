from django.db import models
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from login.models import User
import datetime

class Patient(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    identifier = models.CharField(max_length=20)
    sex = models.CharField(max_length=20)
    blood_type = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Date(models.Model):
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class Appointment(models.Model):
    treatment_type = models.CharField(max_length=20)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    date = models.ForeignKey(Date, on_delete=models.CASCADE, null=True)

class Room(models.Model):
    number = models.IntegerField()
    bed = models.IntegerField()

    def __str__(self):
        return str(self.number)

class Hospitalization(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    occupied_bed = models.IntegerField(null=True)
    patient = models.OneToOneField(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField(null=True)