from django.urls import path

from . import views


urlpatterns = [
    path('register', views.register_form, name='register_form'),
    path('api/register', views.RegisterAPI.as_view(), name='register'),
    path('auth', views.login_form, name='login_form'),
]
