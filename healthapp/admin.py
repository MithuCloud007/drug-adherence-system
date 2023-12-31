from django.contrib import admin
from .models import Patient,Prescription,Doctor
# Register your models here.
admin.site.register(Patient)
admin.site.register(Prescription)
admin.site.register(Doctor)