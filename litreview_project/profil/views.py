from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from feed.models import Ticket, Review
from feed.forms import BookForm
from .models import Book

# Create your views here.

@login_required
def profil(request):
	books = Book.objects.filter(user=request.user).order_by('-time_created')
	if books.exists():
		return render(request, 'profil/profil.html', {'books': books})
	else:
		message = "Vous n'avez pas encore de livre dans votre list de souhait"
		return render(request, 'profil/profil.html', {'message': message})


@login_required
def wishlisted(request, ticket_id):
	ticket = Ticket.objects.get(pk=ticket_id)
	new_book = Book(
		title=ticket.title, author="auteur non renseigné", summary="aucun résumé",
		image=ticket.image, user=request.user, ticket_id=ticket_id,
		)
	new_book.save()
	return redirect("profil")


@login_required
def delete_book(request, book_id):
	book = Book.objects.get(pk=book_id)
	book.delete()
	return redirect("profil")

@login_required
def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect("profil")
    else:
        form = BookForm()
    return render(request, "profil/book.html", {"form": form})    

@login_required
def update_book(request, book_id):
	book = Book.objects.get(pk=book_id)
	form = BookForm(request.POST or None, request.FILES or None, instance=book)
	if form.is_valid():
		form.save()
		return redirect("profil")
	return render(request, "profil/book.html", {"form": form })


@login_required
def delete_user(request):
 	user = User.objects.get(username=request.user)
 	#user.delete()
 	return redirect("logout")
