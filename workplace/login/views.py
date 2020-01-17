from django.shortcuts import render
from .forms import Signup, Log
from django.http import HttpResponseRedirect
from .models import Users, Sessions
from django.core.exceptions import ObjectDoesNotExist
from .store import generate_long_random_key
import datetime


def signup(request):
    if request.method == "POST":
        form = Signup(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = Signup()
    return render(request, "users/signup.html", {'form': form})


def login(request):
    if request.method == "POST":
        form = Log(request.POST)
        username = request.POST.get("username")
        password = request.POST.get("password")
        sessionid = loginup(username, password)
        if sessionid:
            response = HttpResponseRedirect('/')
            loginup(username, password)
            response.set_cookie('sessionid', sessionid,)
            return response

    else:
        print("OK")
        form = Log()
    return render(request, 'users/login.html', {'form': form})


def loginup(username, password):
    try:
        user = Users.objects.get(username=username)
    except ObjectDoesNotExist:
        return None
    session = Sessions()
    session.user = user
    session.key = generate_long_random_key()
    session.expires = datetime.datetime.now() + datetime.timedelta(days=1)
    return session.key

