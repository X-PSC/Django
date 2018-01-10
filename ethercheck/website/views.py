from django.shortcuts import render, render_to_response
from website.models import Transaction
from website.models import Alias
from website.models import Block
import requests, json

# Create your views here.

def home(request):
	return render(request, 'index.html', locals())

def transactions(request):
	transactions = Transaction.objects.all()
	return render(request, 'transactions.html', locals())

def blocks(request):
	blocks = Block.objects.all()
	return render(request, 'blocks.html', locals())

def alias(request):
	alias = Alias.objects.all()
	return render(request, 'alias.html', locals())

def graph(request):
	return render(request, 'graph.html', locals())

def graphData(request):
	return render_to_response('graph.gexf')

def tauxChange(request):
	changeInformation=json.loads(requests.get('https://api.coinmarketcap.com/v1/ticker/ethereum/?convert=EUR').text)
	usd=round(float(changeInformation[0]["price_usd"]),2)
	eur=round(float(changeInformation[0]["price_eur"]),2)
	bit=round(float(changeInformation[0]["price_btc"]),8)
	evo_1h=changeInformation[0]["percent_change_1h"]
	if float(evo_1h)>0:
		inc_1h="Increasing"
	else:
		inc_1h="Decreasing"
	evo_24h=changeInformation[0]["percent_change_24h"]
	if float(evo_24h)>0:
		inc_24h="Increasing"
	else:
		inc_24h="Decreasing"
	evo_7d=changeInformation[0]["percent_change_7d"]
	if float(evo_7d)>0:
	   inc_7d="Increasing"
	else:
	   inc_7d="Decreasing"
	return render(request, 'tauxChange.html', locals())
