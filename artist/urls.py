from django.urls import path
from . import views

app_name = "artist"

urlpatterns = [
    path("register", views.RegisterArtistView.as_view(), name="signup"),
    path("dashboard", views.DashboardView.as_view(), name="dashboard"),
]