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
	return render(request, 'registration/register.html', {'form': form})


# Log out user

def disconnect(request):
	logout(request)
	return render(request, 'registration/logout.html')
