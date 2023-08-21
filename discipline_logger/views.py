from django.shortcuts import get_object_or_404, render
import requests

from login.models import User


def index(request):
    return render(request, 'home/index.html')


def dashboard(request):
    data = {}
    session = requests.Session()
    response = session.get(
        "http://127.0.0.1:8000/account/api/user/", auth=('username', 'password'))
    print(session.cookies)
    response = requests.get(
        'http://127.0.0.1:8000/account/api/user', json=data)
    print(response)
    return render(request, 'home/dashboard.html')


# def index(request, user_id):
#     user = get_object_or_404(User, pk=user_id)
#     return render(request, 'home/index.html', {'user': user})
