from re import template
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')