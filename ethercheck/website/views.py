from django.shortcuts import render, render_to_response
from website.models import Transaction
from website.models import Alias
import requests, json

# Create your views here.

def home(request):
	return render(request, 'index.html', locals())


def transactions(request):
	transactions = Transaction.objects.all()
	return render(request, 'transactions.html', locals())

def alias(request):
	alias = Alias.objects.all()
	return render(request, 'alias.html', locals())

def graph(request):
	return render(request, 'graph.html', locals())

def graphData(request):
	return render_to_response('graphData.json',content_type='application/json')

def tauxChange(request):
	text=json.loads(request.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/?convert=EUR'))
	
	return render(request, 'tauxChange.html', locals())
