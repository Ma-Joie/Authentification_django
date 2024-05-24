from django.contrib import messages
from django.shortcuts import render , redirect
from .form import CustomUserCreationForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login , authenticate
# Create your views here.

def inscription(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')
    else:
        form = CustomUserCreationForm()
    return render(request , 'inscription.html' , {'form': form})


def connexion(request):
    if request.method == 'POST':
        name = request.POST["user_name"]
        password = request.POST["password"]
        user = authenticate(request, name=name , password = password)
        if user is not None:
            login(request , user)
            return redirect('accueil')
    else:
        messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request , 'connexion.html' )    