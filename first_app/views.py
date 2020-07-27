from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello Django!")


def home(request):
    return render(request, "first_app/home.html")