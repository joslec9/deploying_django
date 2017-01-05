from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.sessions.models import Session
from .models import User
import re


# Create your views here.
def index(request):
    context = {
        'user': User.objects.all(),

    }
    return render(request, "login_registration/index.html", context)


def sign_up(request):
    if request.POST:
        new_user = User.objects.create_user(request.POST)
        if new_user[0]:
            request.session['user'] = {
                'name': new_user[1].first_name + ' ' + new_user[1].last_name,
                'id': new_user[1].id
            }
            context = {
                'user': new_user[1],
            }
            return render(request, "login_registration/success.html", context)
        else:
            for error in new_user[1]:
                messages.warning(request, error)
    return redirect('/')


def login(request):
    login_user = User.objects.login_user(request.POST)
    if login_user[0]:
        request.session['user'] = {
            'name': login_user[1].first_name + ' ' + login_user[1].last_name,
            'id': login_user[1].id
        }
        context = {
            'user': login_user[1],
        }
        return render(request, "login_registration/success.html", context)
    else:
        for error in login_user[1]:
            messages.warning(request, error)
    return redirect('/')


def logout(request):
    Session.objects.all().delete()
    return redirect('/')


def remove(request, id):
    User.objects.filter(id=id).delete()
    return redirect('/')


def account(request):
    context = {
        'user': User.objects.all(),

    }
    return render(request, "login_registration/account.html", context)