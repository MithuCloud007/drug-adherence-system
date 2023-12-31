from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin
from django.views.generic import CreateView,UpdateView,ListView,DetailView,DeleteView
from .models import Prescription,Doctor
from .forms import PrescriptionForm

    
class AddPrescription(CreateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'healthapp/add.html'
    success_url= reverse_lazy('healthapp:all_prescription') 
    
class AllPrescription(ListView):
    model = Prescription
    context_object_name = 'prescription'
    template_name = 'healthapp/all.html'  
    
class UpdatePrescription(UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'healthapp/update.html'
    success_url= reverse_lazy('healthapp:all_prescription') 
    
class ViewPrescription(DetailView):
    model = Prescription
    context_object_name = 'prescription'
    template_name = 'healthapp/view.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['doctor_object'] = Doctor.objects.get(pk=1)
        # Add more context objects as needed

        return context
    
class DeletePrescription(DeleteView):
    model = Prescription 
    template_name = 'healthapp/prescription_confirm_delete.html' 
    success_url= reverse_lazy('healthapp:all_prescription')     
      
