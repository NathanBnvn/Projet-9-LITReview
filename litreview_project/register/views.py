from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from .forms import LogInForm, SignUpForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

# view that manage login 
def login(request):
	form = LogInForm
	#AuthenticationForm()
	if request.method == 'POST':
		connect(request)
	return render(request, 'register/login.html', {'form': form })

# view for register new user
def register(request):
	form = SignUpForm()
	#UserCreationForm()
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		#UserCreationForm(request.POST)
		if form.is_valid():
			print('202')
			#form.save()
			connect(request)
		else:
			print('402')
	else:
		form = SignUpForm() 
		#UserCreationForm()
	return render(request, 'register/register.html', {'form': form})

# function to log user
def connect(request):
	username = request.POST.get('username')
	password = request.POST.get('password1')
	user = authenticate(request, username=username, password=password)
	print(username) 
	print(user)

	if user is not None:
		#login(request, user)
		print('204')
		# Redirect to a success page.
		return redirect(settings.LOGIN_REDIRECT_URL, request.path)
	else:
		# Return an 'invalid login' error message.
		#messages.error(request, 'Invalid login')
		print('404')

# function to log out
def logout(request):
	logout(request)
	return redirect(settings.LOGIN_URL, request.path)
