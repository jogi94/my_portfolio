from django.urls import path
from .views import LoginActivityView
from django.contrib.auth.decorators import login_required

app_name = "loginActivities"

urlpatterns = [
    path('', login_required(LoginActivityView.as_view()), name='login_activites'),
]
