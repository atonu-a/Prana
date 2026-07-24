from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



# Create your views here.

# Sign in page
def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password!")
            
    return render(request, "login.html")

#profile page

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

