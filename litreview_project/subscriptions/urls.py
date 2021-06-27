from django.urls import path
from . import views

urlpatterns = [
	path('', views.subscriptions, name='subscriptions'),
	path('chercher/', views.search, name='search'),
	path('abonner/<user>', views.subscribe, name='subscribe'),
	path('desabonner/<follow_id>', views.unsubscribe, name='unsubscribe')
]