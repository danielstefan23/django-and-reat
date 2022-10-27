from typing import _SpecialForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import PatientForm, AppointmentForm, HospitalizationForm
from login.models import User
from .models import Patient, Date, Appointment, Room, Hospitalization
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import datetime


@login_required(login_url='/account/login/')
def homepage(request):
    return render(request, 'site/index.html', {})

@login_required(login_url='/account/login/')
def profile_page(request):
    current_user = request.user
    return render(request, 'site/profile.html', {'current_user': current_user})

@login_required(login_url='/account/login/')
def profiles(request, pk):
    profile = User.objects.get(pk = pk)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('homepage')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'site/profile.html', {'current_user': profile, 'form': form})

@login_required(login_url='/account/login/')
def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PatientForm()
    return render(request, 'site/adauga_pacient.html', {'form': form})

@login_required(login_url='/account/login/')
def blankets(request):
    return render(request, 'site/paturi.html', {})

@login_required(login_url='/account/login/')
def appointments(request):
    treatments = User.objects.filter(job = 'Doctor').order_by('specializare').values_list('specializare').distinct()
    date = Date.objects.all()
    patients = Patient.objects.all()
    noAppointmentPatients = []
    
    for patient in patients:
        try:
            if (patient.appointment):
                pass
        except:
                noAppointmentPatients.append(patient)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'site/programari.html', {'form': form, 'treatments': treatments, 'patients': noAppointmentPatients, 'dates': date})

@login_required(login_url='/account/login/')
def show_doctors(request):
    doctors = User.objects.filter(job = 'Doctor')
    return render(request, 'site/afiseaza_job.html', {'jobs': doctors, 'title': 'Doctori'})

@login_required(login_url='/account/login/')
def show_nurses(request):
    nurses = User.objects.filter(job = 'Asistenta')
    return render(request, 'site/afiseaza_job.html', {'jobs': nurses, 'title': 'Asistente'})

@login_required(login_url='/account/login/')
def show_appointments(request):
    appointments = Appointment.objects.all()
    return render (request, 'site/afiseaza_programari.html', {'appointments': appointments})

@login_required(login_url='/account/login/')
def delete_appointment(request, pk):
    appointment = Appointment.objects.get(pk = pk)
    if request.method == 'POST':
        appointment.delete()
        return redirect('show_appointments')

@login_required(login_url='/account/login/')
def load_doctors(request):
    treatment = request.GET.get('treatment_type')
    doctors = User.objects.filter(job = 'Doctor').filter(specializare = treatment)
    return render(request, 'dynamic/dropdown_list_options.html', {'doctors': doctors})

@login_required(login_url='/account/login/')
def load_days(request):
    patient = request.GET.get('patient')
    hospitalization_day = Patient.objects.filter(identifier = patient)[0].hospitalization.admission_date
    days = (datetime.date.today() - hospitalization_day).days
    return render(request, 'dynamic/load_days.html', {'days': days})

@login_required(login_url='/account/login/')
def load_payment(request):
    days = str(request.GET.get('days'))
    payment = 500 * int(days)
    return render(request, 'dynamic/load_payment.html', {'payment': payment})

@login_required(login_url='/account/login/')
def rooms(request):
    rooms = Room.objects.filter(bed = 1)
    patients = Patient.objects.all()
    noRoomPatients = []
    
    for patient in patients:
        try:
            if (patient.hospitalization):
                pass
        except:
                noRoomPatients.append(patient)

    noRoom = []
    hospitalizations = Hospitalization.objects.all()
    for room in rooms:
        flag = False
        for hospitalization in hospitalizations:
            if (room == hospitalization.room):
                flag = True
                break
        if (flag == False):
            noRoom.append(room)

    if request.method == 'POST':
        form = HospitalizationForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.admission_date = datetime.date.today()
            room.occupied_bed = 1
            room.save()
            return redirect('homepage')
    else:
        form = HospitalizationForm()
    return render(request, 'site/camere.html', {'form': form, 'rooms': noRoom, 'patients': noRoomPatients})

@login_required(login_url='/account/login/')
def show_hospitlizations(request):
    hospitalizations = Hospitalization.objects.all()
    return render (request, 'site/afiseaza_internari.html', {'hospitalizations': hospitalizations})

@login_required(login_url='/account/login/')
def delete_hospitlization(request, pk):
    hospitalization = Hospitalization.objects.get(pk = pk)
    if request.method == 'POST':
        hospitalization.delete()
        return redirect('show_hospitlizations')

@login_required(login_url='/account/login/')
def process_payments(request):
    patients = Patient.objects.all()
    hospitalizationPatients = []
    
    for patient in patients:
        try:
            if (patient.hospitalization):
                hospitalizationPatients.append(patient)
        except:
            pass
    
    return render (request, 'site/plati.html', {'patients': hospitalizationPatients})