from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("user.urls")),
    path("artist/", include("artist.urls")),
    path("manager/", include("manager.urls")),
]
