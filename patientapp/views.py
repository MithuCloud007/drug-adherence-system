from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from healthapp.models import Patient
from healthapp.forms import PatientForm
    
class AddPatient(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patientapp/add.html'
    success_url= reverse_lazy('patientapp:all_patient')    

class AllPatient(ListView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'patientapp/all.html'  
    
class UpdatePatient(UpdateView):
    model = Patient
    form_class = PatientForm
    template_name = 'patientapp/update.html'
    success_url= reverse_lazy('patientapp:all_patient') 
    
class ViewPatient(DetailView):
    model = Patient
    context_object_name = 'patient'
    template_name = 'patientapp/view.html'
    
class DeletePatient(DeleteView):
    model = Patient 
    template_name = 'patientapp/patientapp_confirm_delete.html' 
    success_url= reverse_lazy('patientapp:all_patient')                    