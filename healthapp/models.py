from django.db import models

from django.db import models

class Doctor(models.Model):
    doctor_id = models.CharField(max_length=255, default='d00x')
    doctor_name = models.CharField(max_length=255)
    doctor_designation = models.CharField(max_length=100)
    doctor_contact_number = models.CharField(max_length=15)

    def __str__(self):
        return self.doctor_name


class Patient(models.Model):
    PATIENT_CATEGORIES = [
        ('Inpatient', 'Inpatient'),
        ('Outpatient', 'Outpatient'),
        ('Pediatric', 'Pediatric'),
        ('Geriatric', 'Geriatric')
    ]
    patient_id = models.CharField(max_length=50,default='p00x')
    patient_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    patient_category = models.CharField(max_length=50, choices=PATIENT_CATEGORIES)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE, default=1) 
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    diagnostic_center = models.CharField(max_length=255)
    
    def __str__(self):
        return self.patient_name 

class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    MEDICINE_NAME = [
        ('isoniazid', 'Isoniazid'),
        ('rifampin ', 'Rifampin '),
        ('pyrazinamide ', 'Pyrazinamide'),
         ('ethambutol', 'Ethambutol '),
        ('streptomycin ', 'Streptomycin'),
    ]
    drug_name = models.CharField(max_length=200,choices=MEDICINE_NAME)
    description = models.TextField(blank=True)
    TAKEN_SLOT = [
        ('morning', 'Morning'),
        ('midday', 'Midday'),
        ('night', 'Night'),
    ]
    taken_time1 = models.CharField(max_length=200, choices=TAKEN_SLOT,null=True,blank=True)
    taken_time2 = models.CharField(max_length=200, choices=TAKEN_SLOT,null=True,blank=True)
    taken_time3 = models.CharField(max_length=200, choices=TAKEN_SLOT,null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)

    def __str__(self):
        return f"{self.patient.patient_name}'s Prescription for {self.drug_name}"
    

    
    
