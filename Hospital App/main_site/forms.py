from django import forms
from .models import Patient, Appointment, Room, Hospitalization
from login.models import User

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'identifier', 'sex', 'blood_type')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('treatment_type', 'doctor', 'patient', 'date')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['doctor'].queryset = User.objects.none()

        if 'treatment_type' in self.data:
            try:
                treatment = self.data.get('treatment_type')
                self.fields['doctor'].queryset = User.objects.filter(job = 'Doctor').filter(specializare = treatment)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['doctor'].queryset = self.instance.treatment.doctor_set.order_by('name')

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('treatment_type', 'doctor', 'patient', 'date')

class HospitalizationForm(forms.ModelForm):
    class Meta:
        model = Hospitalization
        fields = ('room', 'patient')