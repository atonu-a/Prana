from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    music = AudioMediations.objects.all()
    
    data = {
        'music':music
    }
    return render(request, "index.html", data)

