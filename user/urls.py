from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.UserView.as_view(), name='signup'),
    path('login-out', views.UserApiView.as_view(), name='login_out'),
    path('', views.IndexView.as_view(), name='index')
]