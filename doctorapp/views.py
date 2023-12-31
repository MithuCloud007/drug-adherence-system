from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from healthapp.models import Doctor
from healthapp.forms import DoctorForm
    
class AddDoctor(CreateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctorapp/add.html'
    success_url= reverse_lazy('doctorapp:add_doctor')  
    
class AllDoctor(ListView):
    model = Doctor
    context_object_name = 'doctor'
    template_name = 'doctorapp/all.html'  
    
class UpdateDoctor(UpdateView):
    model = Doctor
    form_class = DoctorForm
    template_name = 'doctorapp/update.html'
    success_url= reverse_lazy('doctorapp:all_doctor') 
    
class ViewDoctor(DetailView):
    model = Doctor
    context_object_name = 'doctor_obj'
    template_name = 'doctorapp/view.html'
    success_url= reverse_lazy('doctorapp:all_doctor') 
    
class DeleteDoctor(DeleteView):
    model = Doctor 
    template_name = 'doctorapp/doctorapp_confirm_delete.html' 
    success_url= reverse_lazy('doctorapp:all_doctor')                    