from django.urls import path
from .views import AddPrescription,AllPrescription,ViewPrescription,UpdatePrescription,DeletePrescription


app_name='healthapp'

urlpatterns = [
    path('add-prescription', AddPrescription.as_view(), name="add_prescription"),
     path('all-prescription', AllPrescription.as_view(), name="all_prescription"),
    path('update-prescription/<int:pk>', UpdatePrescription.as_view(), name="update_prescription"),
    path('view-prescription/<int:pk>', ViewPrescription.as_view(), name="view_prescription"),
    path('delete-prescription/<int:pk>', DeletePrescription.as_view(), name="delete_prescription"),
    
]