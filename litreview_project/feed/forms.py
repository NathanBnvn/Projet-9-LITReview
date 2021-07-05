from django import forms
from .models import Review, Ticket
from django.contrib.auth.forms import AuthenticationForm

CHOICES = [(i,i) for i in range(6)]

class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe'}))

class ReviewForm(forms.ModelForm):
	prefix = 'review'
	class Meta:
		model = Review
		fields = ['headline','rating','body']
		labels = {
			'headline': ('Titre'),
			'rating': ('Note'),
			'body': ('Commentaire'),
		}
		widgets = {
            'rating': forms.RadioSelect(choices=CHOICES, attrs={'display':'inline'}),
        }

class TicketForm(forms.ModelForm):
	prefix = 'ticket'
	class Meta:
		model = Ticket
		fields = ['title', 'description', 'image']
