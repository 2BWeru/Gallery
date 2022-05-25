from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
def navbar(request):
    return render(request,'navbar.html')

def home(request):
    return render(request,'home.html')


