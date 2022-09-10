from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.UserView.as_view(), name='signup'),
    path('login', views.UserApiView.as_view(), name='login'),
    path('', views.IndexView.as_view(), name='index')
]