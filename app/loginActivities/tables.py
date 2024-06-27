import django_tables2 as tables
from login_history.models import LoginHistory


class LoginActivitesTable(tables.Table):
    status = tables.Column(empty_values=(), verbose_name="Status")
    status_with_time = tables.Column(empty_values=(), verbose_name="Status with Time")

    class Meta:
        model = LoginHistory
        fields = ("user", "date_time", "is_login", "is_logged_in")

    def render_status(self, value, record):
        if record.is_login:
            return "Logged In" if record.is_logged_in else "Logged Out"
        return "Logged Out"

    def render_status_with_time(self, value, record):
        status = "Logged In" if record.is_login else "Logged Out"
        return f"{status} at {record.date_time.strftime('%Y-%m-%d %H:%M:%S')}"
