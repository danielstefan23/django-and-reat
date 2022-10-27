from django.urls import path
from . import views
from django.contrib.auth import views as defaultViews

urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('account/login/', defaultViews.LoginView.as_view(), name='login'),
    path('account/logout/', defaultViews.LogoutView.as_view(next_page='/'), name='logout'),
    path('add/patient/', views.add_patient, name='add_patient'),
    path('rooms/', views.rooms, name='rooms'),
    path('blankets/', views.blankets, name='blankets'),
    path('appointments/', views.appointments, name='appointments'),
    path('payments/', views.process_payments, name='payments'),
    path('doctors/', views.show_doctors, name='show_doctors'),
    path('nurses/', views.show_nurses, name='show_nurses'),
    path('profiles/<int:pk>', views.profiles, name='profiles'),
    path('ajax/load-doctors/', views.load_doctors, name='ajax_load_doctors'),
    path('ajax/load-days/', views.load_days, name='ajax_load_days'),
    path('ajax/load-paymnet/', views.load_payment, name='ajax_load_payment'),
    path('appointments/view/', views.show_appointments, name='show_appointments'),
    path('appointments/delete/<int:pk>', views.delete_appointment, name='delete_appointment'),
    path('hospitalizations/view/', views.show_hospitlizations, name='show_hospitlizations'),
    path('hospitalizations/delete/<int:pk>', views.delete_hospitlization, name='delete_hospitlization'),
]