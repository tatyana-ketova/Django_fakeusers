from django.shortcuts import render

from django.http import HttpResponse
from userapp.models import User

# Create your views here.


def user_view(request):
    users = User.objects.all()

    return render(request, 'users.html', {'users': users})
# Create your views here.
def index(request):


    return render(request, 'index.html')