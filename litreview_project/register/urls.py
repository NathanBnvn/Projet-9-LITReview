from django.urls import path
from django.contrib.auth.views import LoginView
from feed.forms import LoginForm
from . import views

urlpatterns = [
    path(
        "",
        LoginView.as_view(
            authentication_form=LoginForm,
            redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("register/", views.register, name="register"),
    path("logout/", views.disconnect, name="logout"),
]
