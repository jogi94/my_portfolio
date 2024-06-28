from django.urls import path
from .views import *

app_name = "company"


urlpatterns = [
    path('company/create/', CompanyCreateView.as_views(), name='company_create'),
]
