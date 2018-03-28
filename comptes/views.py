# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


from .forms import InscriptionForm, EditProfileForm

def home(request):
    return render(request, 'comptes/home.html', {})

def login(request):
    return render(request, 'comptes/login.html', {})

def register(request):
    if request.method =='POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compte:home')
    else:
        form = InscriptionForm()
    context = {
        'form': form,
    }
    return render(request, 'comptes/register.html', context)

@login_required
def profile(request):
    context = {
        'user':request.user,
    }
    return render(request, 'comptes/profile.html', context)

@login_required
def edit(request):
    instance = request.user
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('comptes:profile')
    else:
        form = EditProfileForm(instance=instance)
    context = {
        'form':form,
        'instance':instance,
    }
    return render(request, 'comptes/edit.html', context)

@login_required
def passe_change(request):
    user = request.user
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('comptes:profile')
        else:
            return redirect('comptes:passe_change')
    else:
        form = PasswordChangeForm(user=user)
    context = {
        'form':form,
        'user':user,
    }
    return render(request, 'comptes/passe_change.html', context)







# Create your views here.
