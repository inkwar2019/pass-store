from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from .models import Password


def home(request):
    return render(request, "root/home.html")


def password_generate(request):
    return render(request, "root/password_generate.html")


class PasswordList(ListView):
    model = Password
    paginate_by = 10
    template_name = "root/password_list.html"
    ordering = ['-datetime']


class PasswordDetails(DetailView):
    model = Password
    template_name = "root/password_details.html"


class PasswordCreate(CreateView):
    model = Password
    template_name = "root/password_create.html"
    fields = ['title', 'username', 'password']


class PasswordUpdate(UpdateView):
    model = Password
    template_name = "root/password_update.html"
    fields = ['title', 'username', 'password']
