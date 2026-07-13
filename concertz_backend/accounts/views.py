from django.http import HttpResponse
from .models import User
# Create your views here.

def index(request):
    return HttpResponse("Sounds fine")

def user(request):
    u = User.objects.values("age", "f_name")
    return HttpResponse(f"{u}")