from django.urls import path
from . import views

urlpatterns = [
    path('profile/',views.profile, name="profile"),
    path('login-page/',views.login_view, name="login_view"),
    
]