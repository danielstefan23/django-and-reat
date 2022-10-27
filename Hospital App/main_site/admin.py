from django.contrib import admin
from .models import Patient, Appointment, Date, Room, Hospitalization

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'identifier', 'blood_type', 'sex')

admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('treatment_type', 'doctor', 'patient', 'date')

admin.site.register(Appointment, AppointmentAdmin)

class DateAdmin(admin.ModelAdmin):
    list_display = ('date',)

admin.site.register(Date, DateAdmin)

class HospitalizationAdmin(admin.ModelAdmin):
    list_display = ('patient', 'admission_date', 'room', 'occupied_bed')

admin.site.register(Hospitalization, HospitalizationAdmin)

class RoomAdmin(admin.ModelAdmin):
    list_display = ('number', 'bed')

admin.site.register(Room, RoomAdmin)