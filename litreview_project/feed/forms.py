from django import forms
from .models import Review, Ticket

class ReviewForm(forms.ModelForm):

	class Meta:
		model = Review
		fields = ['headline','rating','body']
		labels = {
			'headline': ('titre'),
			'rating': ('note'),
			'body': ('commentaire'),
		}
		#widgets = {
		#	'rating': forms.RadioSelect()
		#}

class TicketForm(forms.ModelForm):
	class Meta:
		model = Ticket
		fields = ['title', 'description', 'image']
