from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import *

# Create your views here.
def profile(request):
    return render(request, "profile.html")