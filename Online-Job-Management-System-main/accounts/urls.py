from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
# from accounts.views import send_email_to_client #->

from jobsapp.views import EditProfileView
from .views import *

app_name = "accounts"

urlpatterns = [
    path('employee/register', RegisterEmployeeView.as_view(), name='employee-register'),
    path('employer/register', RegisterEmployerView.as_view(), name='employer-register'),
    path('employee/profile/update', EditProfileView.as_view(), name='employer-profile-update'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),
    # path('send-job-email/', send_email_to_client, name='send_job_email'),
    path('send-email/', views.send_email, name='send_email'),
    path('accounts:resume/<int:user_id>/', views.generate_resume, name='generate_resume'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




