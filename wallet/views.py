from django.shortcuts import render, redirect
from django.contrib import messages 

# Import Wallet Model
from wallet.models import Wallet

# Import Transaction Model
from transaction.models import Transaction

# Import Wallet Form
from wallet.forms import WalletForm

def home(request):
	user = request.user
	wals = Wallet.objects.filter(user_id = user.id)
	trans = Transaction.objects.filter(receive_user = user.username).values()
	requs = Transaction.objects.filter(send_user = user.username).values()
	if len(wals):
		wal = wals.get(user_id = user.id)
		return render(request, 'wallet.html', {'wal':wal, 'trans': trans, 'requs': requs})
	else:
		return render(request, 'wallet.html', {})

def form(request):
	wal = Wallet(user_id=request.user.id, balance=1000, monetary_unit='$')
	wal.save()
	return redirect('/wallet/')
	
def change(request, id):
	if request.method == 'POST':
		user = request.user
		wal = Wallet.objects.get(user_id = user.id)
		wal.monetary_unit = id
		wal.save()
	return redirect('/wallet/')

def transfer(request):
	if request.method == 'POST':
		messages.success(request, ('Receiver wallet is not created'))
		return redirect('/wallet/')
