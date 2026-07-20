from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def profile(request):
    profile = request.user.profile
    languages = Language.objects.all()
    if request.method == 'POST':
        profile.full_name = request.POST.get('full_name')
        profile.email = request.POST.get('email')
        profile.gender = request.POST.get('gender')
        profile.nationality = request.POST.get('nationality')
        profile.birthday = request.POST.get('birthday')
        profile.language = request.POST.get('language')
        
        profile.save()
        return redirect('profile')
        
    data = {
        'profile' : profile,
        'languages' : languages,
        
        
    }
    
    return render(request, "profile.html", data)