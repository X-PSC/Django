from django.shortcuts import render
from website.models import Transaction
from website.models import Alias

# Create your views here.

def home(request):
	return render(request, 'index.html', locals())


def transactions(request):
	transactions = Transaction.objects.all()
	return render(request, 'transactions.html', locals())

def alias(request):
	alias = Alias.objects.all()
	return render(request, 'alias.html', locals())

def tauxConversion(request):
	return render(request, 'tauxConversion.html', locals())

def graph(request):
	return render(request, 'graph.html', locals())