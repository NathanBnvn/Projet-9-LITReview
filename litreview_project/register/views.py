from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

# View for register new user

def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect(settings.LOGIN_REDIRECT_URL, request.path)
	else:
		form = UserCreationForm()
		form.fields['username'].widget.attrs.update({
			'placeholder': "Nom d'utilisateur"
			})
		form.fields['password1'].widget.attrs.update({
			'placeholder': "Mot de passe"
			})
		form.fields['password2'].widget.attrs.update({
			'placeholder': "Confirmer mot de passe"
			})
	return render(request, 'registration/register.html', {'form': form})


# Log out user

def disconnect(request):
	logout(request)
	return render(request, 'registration/logout.html')
