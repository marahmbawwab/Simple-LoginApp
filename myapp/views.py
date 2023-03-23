from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import urls
from .models import User_Details
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.


def login(request):
    if request.method == 'POST':
        # features = User_Details.objects.all()
        username = request.POST['user']
        password = request.POST['pass']

        user = auth.authenticate(username=username, password=password)

        if (user is not None):
            auth.login(request, user)
            # welcome to our website
            return redirect('/')
        else:
            messages.info(
                request, "You don't have an account!. Please signup.")
            return redirect('/login')

    else:
        return render(request, 'login.html')


def welcome(request):
    return render(request, 'welcome_page.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['pass']
        email = request.POST['email']

        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Exists.')  # throw an error
            return redirect('/signup')
        elif User.objects.filter(username=username).exists():
            # throw an error
            messages.info(request, 'User Already registered.')
            return redirect('/signup')
        else:
            user = User.objects.create_user(
                username=username, email=email, password=password)
            user.save()
            return redirect('/')
    else:
        return render(request, 'signup.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
