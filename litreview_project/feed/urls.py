from django.urls import path
from . import views

urlpatterns = [
	path('', views.feed, name='feed',),
	path('create-review', views.create_review, name='create-review'),
	path('ask-review', views.ask_review, name='ask-review')
]