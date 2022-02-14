from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import views as auth_views, forms as auth_forms
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import CustomUserCreationForm


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class ChangePasswordResetDoneView(auth_views.PasswordChangeView):
    #form_class = auth_forms.PasswordChangeForm
    template_name = 'password_change_form.html'
    success_url = reverse_lazy('password_change_done')


class ChangePasswordResetDoneSuccessView(auth_views.PasswordChangeView):
    #form_class = auth_forms.PasswordChangeForm
    template_name = 'password_change_done.html'


