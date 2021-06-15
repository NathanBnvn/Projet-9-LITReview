from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django import forms

class LogInForm(AuthenticationForm):
	username = UsernameField(
		label = (""),
		widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom d\'utilisateur'})
		)
	password = forms.CharField(
		label = (""),
		widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Mot de passe'})
		)
	

class SignUpForm(UserCreationForm):
	username = forms.CharField(
		label = (""),
		widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nom d\'utilisateur'})
		)
	password1 = forms.CharField(
		label = (""),
		widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Mot de passe'}))
	password2 = forms.CharField(
		label = (""),
		widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirmer mot de passe'}))
