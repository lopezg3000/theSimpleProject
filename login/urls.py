from django.urls import path
from .views import LoginAPI, UserAPI

from . import views
from knox import views as knox_views


urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/register/', views.RegisterAPI.as_view(), name='register'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('register', views.register_form, name='register_form'),
    path('auth', views.login_form, name='login_form'),
]
