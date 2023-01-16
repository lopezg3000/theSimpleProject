from django.shortcuts import get_object_or_404, render

from login.models import User


def index(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'home/index.html', {'user': user})
