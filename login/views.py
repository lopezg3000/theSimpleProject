# django imports
import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login


from rest_framework.response import Response
from rest_framework import generics, authentication, permissions
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .serializers import UserSerializer, RegisterSerializer, AuthSerializer
from rest_framework.authentication import SessionAuthentication

from knox.models import AuthToken
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView

from .forms import RegisterForm
from .forms import LoginForm


def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            requests.post(
                'http://127.0.0.1:8000/account/api/register/', json=form.data)
            return HttpResponseRedirect('auth')
    else:
        form = RegisterForm()
    return render(request, 'login/register.html', {'form': form})


def login_form(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            requests.post(
                'http://127.0.0.1:8000/account/api/login/', json=form.data)
            # data = request.COOKIES['auth_token']
            # print(data)

            return HttpResponseRedirect('http://127.0.0.1:8000/home')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


# Register API

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]})


# Login API

class LoginView(KnoxLoginView):
    serializer_class = AuthSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)

        # response = super(LoginAPI, self).post(request, format)

        # token = response.data['token']
        # del response.data['token']
        # response.set_cookie(
        #     'auth_token',
        #     token,
        #     httponly=True,
        #     samesite='strict',
        # )

        # return response


# Get User API
class UserAPI(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
