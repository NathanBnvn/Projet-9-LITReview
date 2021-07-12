from django.urls import path
from . import views

urlpatterns = [
    path("", views.show_posts, name="posts"),
    path(
        "modifier-ticket/<post_id>",
        views.update_ticket,
        name="update-ticket"
    ),
    path(
        "modifier-critique/<post_id>",
        views.update_review,
        name="update-review"),
    path(
        "supprimer-ticket/<post_id>",
        views.erase_ticket,
        name="erase-ticket"
    ),
    path(
        "supprimer-critique/<post_id>",
        views.erase_review,
        name="erase-review"
    ),
]
