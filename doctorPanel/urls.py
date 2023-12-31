from django.urls import path

from doctorPanel.views import doctorpanel

app_name='doctorPanel'

urlpatterns = [
    path('doc-panel', doctorpanel, name="doc_panel"),
    # path('profile/<int:pk>', UserProfileDetailView.as_view(), name='profile_page'),
    # path('login/', login_view, name='login_page'),
    # path('logout/', logoutuser, name='logout_page'),
]