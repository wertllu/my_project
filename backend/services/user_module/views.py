from django.shortcuts import redirect, render
from services.user_module.forms import ProfileForm
from utils.send_email import send_email
from settings import SITE_URL
from services.user_module.forms import AuthForm, RegistrationForm
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.db import models
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password

User = get_user_model()
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

    
def registration(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(email=form.data['email'],
                                            username=form.data['username'], 
                                            password=form.data['password'])

            user.first_name=form.data['first_name']
            user.last_name=form.data['last_name']

            user.save()
            return redirect('auth')

    else:
        form = RegistrationForm()
        return render(request, 'registration.html')

def auth(request):
    if request.method=="POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username'], 
                                password=form.data['password'])
            if user is not None:
                login(request, user)

                return redirect('index')
            else:
                # send_email(subject='tet', body='tet', recipients=[''])
                form = AuthForm()
                return render(request, 'auth.html', context={'form': form, 'SITE_URL': SITE_URL })
    else:
        form = AuthForm()

        return render(request, 'auth.html', context={'form': form, 'SITE_URL': SITE_URL })
    
    
def profile(request):
    if request.method=="POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(email=form.data['email'],
                                            username=form.data['username'], 
                                            password=form.data['password'])

            user.first_name=form.data['first_name']
            user.last_name=form.data['last_name']

            user.save()
            return redirect('auth')


    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            user = request.user

            user.first_name=form.data['first_name']
            user.last_name=form.data['last_name']
           
            if not User.objects.filter(email=form.data['email']).exists:
                user.email=form.data['email']

            if not User.objects.filter(username=form.data['username']).exists:
                user.username=form.data['username']

            if form.data['password_old'] and form.data['password_new'] and user.check_password(form.data['password_old']):
                user.password = make_password(form.data['password_new'])

            
            user.save()
            return redirect('profile')
        else:
            return render(request, 'profile.html',context={'form': form } )

    else:
        form = ProfileForm(data={'first_name': request.user.first_name,
                                 'last_name': request.user.last_name,
                                 'username': request.user.username,
                                 'email': request.user.email,})

        return render(request, 'profile.html', context={'form': form })