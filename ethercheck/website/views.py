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
	return render_to_response('graph.gexf')

def tauxChange(request):
	changeInformation=json.loads(requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR').text)
	usd=changeInformation[0]["price_usd"]
	eur=changeInformation[0]["price_eur"]
	bit=changeInformation[0]["price_btc"]
	evo_1h=changeInformation[0]["percent_change_1h"]
	evo_24h=changeInformation[0]["percent_change_24h"]
	evo_7d=changeInformation[0]["percent_change_7d"]
	return render(request, 'tauxChange.html', locals())
