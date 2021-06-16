from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def subscriptions():
	pass

def search(request):
	#query = request.GET.get('query')
	pass
	# verifier la doc pour les orm de filtrage
	# https://docs.djangoproject.com/en/3.2/topics/db/queries/ 
	#user = UserClass.objects.filter(name__icontains=query)