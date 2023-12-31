# serializers.py
from rest_framework import serializers
from healthapp.models import Doctor, Patient, Prescription

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer() 
    class Meta:
        model = Patient
        fields = '__all__'

class PrescriptionSerializer(serializers.ModelSerializer):
    patient = PatientSerializer() 
    class Meta:
        model = Prescription
        fields = '__all__'

   