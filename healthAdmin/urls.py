from django.urls import path

from healthAdmin.views import dashboard

app_name='healthAdmin'

urlpatterns = [
	path('', dashboard, name="dashboard"),
    # path('profile/<int:pk>', UserProfileDetailView.as_view(), name='profile_page'),
    # path('login/', login_view, name='login_page'),
    # path('logout/', logoutuser, name='logout_page'),
]