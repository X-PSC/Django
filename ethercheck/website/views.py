from django.shortcuts import render
from website.models import Transaction

# Create your views here.

def home(request):
	transactions = Transaction.objects.all()
	return render(request, 'index.html', locals())

