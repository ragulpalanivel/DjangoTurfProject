from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomLoginForm, CustomRegistrationForm
from django.contrib.auth import login
from .forms import CustomRegistrationForm, OTPForm
from django.core.mail import send_mail
import random

class CustomLoginView(LoginView):
    template_name = 'signin.html'
    form_class  = CustomLoginForm
    

class UserRegisterView(CreateView):
    model = User 
    form_class = CustomRegistrationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('signin') 

