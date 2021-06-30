from django import forms
from .models import Review, Ticket

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
		#widgets = {
		#	'rating': forms.RadioSelect()
		#}

class TicketForm(forms.ModelForm):
	prefix = 'ticket'
	class Meta:
		model = Ticket
		fields = ['title', 'description', 'image']
