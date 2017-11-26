from django.shortcuts import render
from website.models import Transaction

# Create your views here.

def home(request):
	return render(request, 'index.html', locals())


def transactions(request):
	transactions = Transaction.objects.all()
	return render(request, 'transactions.html', locals())

def alias(request):
	alias = Alias.objects.all()
	return render(request, 'alias.html', locals())
