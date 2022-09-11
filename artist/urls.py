from django.urls import path
from . import views

urlpatterns = [
    path("register", views.RegisterArtistView.as_view(), name="new_artist"),
]