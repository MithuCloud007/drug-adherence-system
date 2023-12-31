from django.urls import path
from .views import AddDoctor,AllDoctor,UpdateDoctor,ViewDoctor,DeleteDoctor


app_name='doctorapp'

urlpatterns = [
    path('add-doctor', AddDoctor.as_view(), name="add_doctor"),
    path('all-doctor', AllDoctor.as_view(), name="all_doctor"),
    path('update-doctor/<int:pk>', UpdateDoctor.as_view(), name="update_doctor"),
    path('view-doctor/<int:pk>', ViewDoctor.as_view(), name="view_doctor"),
    path('delete-doctor/<int:pk>', DeleteDoctor.as_view(), name="delete_doctor"),
]