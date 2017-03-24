from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import QuoteForm
from django.utils.timezone import now
from .models import Quote
from django.contrib.auth.models import User
# Create your views here.


@login_required
def overview(request):
	form = QuoteForm()
	quotes = Quote.objects.exclude(favorites=request.user)
	favorite_quotes = request.user.favorite_quotes.all()
	return render(request, "project/overview.html", {'form': form, 'quotes': quotes, 'favorite_quotes':favorite_quotes})


@login_required
def favorite(request, quote_id):
	if request.method == 'POST':
		quote = get_object_or_404(Quote, id=quote_id)
		request.user.favorite_quotes.add(quote)
	return redirect('overview')

@login_required
def remove_favorite(request, quote_id):
	if request.method == 'POST':
		quote = get_object_or_404(Quote, id=quote_id)
		request.user.favorite_quotes.remove(quote)
	return redirect('overview')


@login_required
def create(request):
	form = QuoteForm(request.POST or None)
	if form.is_valid():
		form.instance.user = request.user
		form.save()
		return redirect('overview')
	return render(request, "project/create.html", {'form':form})


@login_required
def edit(request):
	quote = get_object_or_404(Quote, id=id)
	form = QuoteForm(request.POST or None, instance=quote)
	if form.is_valid():
		form.save()
		return redirect('overview')
	return render(request, "project/edit.html", {})


@login_required
def delete(request):
	quote = get_object_or_404(Quote, id=id)
	if request.method == 'POST':
		appointment.delete()
		return redirect('overview')
	return render(request, "project/delete.html", {})

@login_required
def user_quotes(request, user_id):
	user = get_object_or_404(User, id=user_id)
	quotes = Quote.objects.filter(user=user)

	return render(request, "project/user_quotes.html", {'quotes':quotes, 'user':user})