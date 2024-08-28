from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import check_password, make_password, identify_hasher


# Create your views here.

# login
def login_view(request):
    page = 'login'
    
    # verifier si l'utilisateur est deja connecter
    if request.user.is_authenticated:
        return redirect('accueil')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password1')
        
    try:
        user = User.objects.get(email=email)
        
          # Vérifier le mot de passe haché avec Argon2
        if check_password(password, user.password):
            login(request, user)
            return redirect('accueil')
        else:
            messages.error(request, "E-mail et/ou mot de passe incorrect(s).")
            
    except User.DoesNotExist:
        messages.error(request,"utilisateur n'existe pas.")
    except UnboundLocalError:
        messages.error(request, "Veuillez renseigner un email et un mot de passe.")
        
    context = {
        'page':page
    }
    return render(request,'authuser/login_register.html',context)

# register
def register_view(request):
    page = 'register'

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password == password2:
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                login(request, user)
                return redirect('accueil')
            except:
                messages.error(request, "Une erreur est survenue lors de la création du compte.")
        else:
            messages.error(request, "Les mots de passe ne correspondent pas.")

    context = {
        'page': page
    }
    return render(request, 'authuser/login_register.html', context)


# logout
def logout_user(request):
    logout(request)
    return redirect('login')


# profile
def profile(request):
    return render(request,'authuser/profile.html')


# modifier le profile
def modifier_profile(request):
    return render(request,'authuser/modifier_profile.html')
