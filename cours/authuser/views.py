from django.shortcuts import render

# Create your views here.

# login
def login(request):
    return render(request,'authuser/login_register.html')

# egister
def register(request):
    return render(request,'authuser/login_register.html')

# profile
def profile(request):
    return render(request,'authuser/profile.html')


# modifier le profile
def modifier_profile(request):
    return render(request,'authuser/modifier_profile.html')
