from django.urls import path
from . import views

urlpatterns = [
	path('', views.feed, name='feed',),
	path('creer-critique/', views.create_review, name='create-review'),
	path('creer-ticket/', views.create_ticket, name='create-ticket')
]