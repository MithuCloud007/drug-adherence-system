from django import forms
from .models import Patient,Prescription,Doctor


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'doctor_id': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor_name': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor_designation': forms.TextInput(attrs={'class': 'form-control'}),
            'doctor_contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
        

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'patient_id': forms.TextInput(attrs={'class': 'form-control'}),            
            'prescription_date': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'height': forms.TextInput(attrs={'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'class': 'form-control'}),
            'patient_category': forms.Select(attrs={'class': 'form-control'}),
            'doctor_id': forms.Select(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'diagnostic_center': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'
        widgets = {
            'patient': forms.Select(attrs={'class': 'form-control'}),
            'drug_name': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'taken_time1': forms.Select(attrs={'class': 'form-control'}),
            'taken_time2': forms.Select(attrs={'class': 'form-control'}),
            'taken_time3': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'},format='%Y-%m-%d'),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}, format='%Y-%m-%d'),
        }
        labels = {
            'patient': 'Patient Name',
            'drug_name': 'Medicine Name',
            'taken_time1': 'Taken Time1',
            'taken_time2': 'Taken Time2',
            'taken_time3': 'Taken Time3',
        }    