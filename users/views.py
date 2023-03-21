from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse


class SignupView(CreateView):
    template_name = "registration/signup.html"
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse("login")
