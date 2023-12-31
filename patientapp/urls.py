from django.urls import path
from patientapp.views import AddPatient,AllPatient,UpdatePatient,DeletePatient,ViewPatient


app_name='patientapp'

urlpatterns = [
    path('add-patient', AddPatient.as_view(), name="add_patient"),
    path('all-patient', AllPatient.as_view(), name="all_patient"),
    path('update-patient/<int:pk>', UpdatePatient.as_view(), name="update_patient"),
    path('view-patient/<int:pk>', ViewPatient.as_view(), name="view_patient"),
    path('delete-patient/<int:pk>', DeletePatient.as_view(), name="delete_patient"),
]