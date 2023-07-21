from django.shortcuts import render
from django.contrib.auth import update_session_auth_hash, login, authenticate, logout
from django.http import HttpResponseRedirect


# Create your views here.
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
