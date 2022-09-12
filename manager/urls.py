from django.urls import path
from . import views

app_name = "manager"

urlpatterns = [
    path("dashboard", views.DashboardView.as_view(), name="dashboard"),
    path("register-list", views.RegisterListView.as_view(), name="register_list"),
    path("register-list/<int:new_status>", views.RegisterListView.as_view(), name="put_status"),
    path("statistics", views.StatisticsView.as_view(), name="statistics"),
]