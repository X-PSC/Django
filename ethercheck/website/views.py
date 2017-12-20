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
	text=json.loads(request.get('https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR'))
	usd=json.dumps(text)[0]["price_usd"]
	eur=json.dumps(text)[0]["price_eur"]
	bit=json.dumps(text)[0]["price_btc"]
	evo_1h=json.dumps(text)[0]["percent_change_1h"]
	evo_24h=json.dumps(text)[0]["percent_change_24h"]
	evo_7d=json.dumps(text)[0]["percent_change_7d"]
	return render(request, 'tauxChange.html', locals())
