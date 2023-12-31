
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from healthapp import urls as healthurls
from healthAdmin import urls as dashboardurls
from doctorapp import urls as doctorurls
from patientapp import urls as patienturls
from doctorPanel import urls as docpanelurls

from rest_framework.routers import DefaultRouter
from healthapp.api.views import DoctorViewSet, PatientViewSet, PrescriptionViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('doctor/', include(healthurls, namespace='healthapp')),
    path('', include(dashboardurls, namespace='healthAdmin')),
    path('', include(docpanelurls, namespace='doctorPanel')),
    path('', include(doctorurls, namespace='doctorapp')),
    path('', include(patienturls, namespace='patientapp')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)