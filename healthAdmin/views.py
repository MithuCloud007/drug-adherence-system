from django.shortcuts import render
from healthapp.models import Patient,Prescription,Doctor

# Create your views here.
def dashboard(request):
    patient = Patient.objects.all()
    patient_count = patient.count()
    prescription = Prescription.objects.all()
    prescription_count =prescription.count()
    doctor = Doctor.objects.all()
    doctor_count = doctor.count()
    response = {
        'patient':patient_count,
        'prescription':prescription_count,
        'doctor': doctor_count
    }
    return render(request, 'healthAdmin/index.html',response)
