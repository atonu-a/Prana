from django.urls import path
from . import views

urlpatterns = [

    path('login-page/',views.login_view, name="login_view"),
    path('profile/',views.profile, name="profile"),
    
]