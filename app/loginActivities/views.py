from django.shortcuts import render
from django.views.generic import ListView
from login_history.models import LoginHistory
from django_tables2 import SingleTableMixin
from app.loginActivities.tables import LoginActivitesTable
from app.utils.helpers import get_current_user, get_current_request


# Create your views here.
class LoginActivityView(SingleTableMixin, ListView):
    model = LoginHistory
    table_class = LoginActivitesTable
    template_name = "loginactivities/loginactivities_list.html"
    context_object_name = "login_history"  # Optional: Customize context variable name

    def get_queryset(self):
        # Retrieve login records for the current user (or any specific user)
        # FIXME: get_current_user method is not working.
        user = get_current_user()  # Assuming user is authenticated and accessing their own history
        queryset = LoginHistory.objects.filter(user=user).order_by('-date_time')
        # queryset = LoginHistory.objects.all()
        return queryset
