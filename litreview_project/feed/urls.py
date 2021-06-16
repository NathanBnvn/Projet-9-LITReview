from django.urls import path
from . import views

urlpatterns = [
	path('', views.feed, name='feed',),
	path('cree-critique/', views.create_review, name='create-review'),
	path('demande-critique/', views.ask_review, name='ask-review')
]