from django.urls import path
from . import views

urlpatterns = [
    path("", views.profil, name="profil"),
    path("ajouter-livre/", views.create_book, name="listed"),
    path("ajouter-liste/<ticket_id>", views.wishlisted, name="wishlist"),
    path("modifier-liste/<book_id>", views.update_book, name="update_book"),
    path("supprimer-livre/<book_id>", views.delete_book, name="unlisted"),
    path("supprimer-compte/", views.delete_user, name='erase_user'),
]