from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages 
import datetime

# Import Transaction Model
from .models import Transaction
# Import Wallet Model
from wallet.models import Wallet

def home(request):
	if request.method == 'POST':
		send_user = request.user
		receive_user = User.objects.get(username = request.POST['receive_user'])
		amount = request.POST['amount']
		payer_wallet = Wallet.objects.get(user_id = send_user.id)
		if float(amount) > float(payer_wallet.balance):
			messages.success(request, ('Your balance is not charged'))
			return redirect('/wallet/')
		receiver_wallets = Wallet.objects.filter(user_id = receive_user.id)
		if len(receiver_wallets) > 0:
			receiver_wallet = Wallet.objects.get(user_id = receive_user.id)
			payer_wallet.balance = float(payer_wallet.balance) - float(amount)
			receiver_wallet.balance = float(receiver_wallet.balance) + float(amount)
			payer_wallet.save()
			receiver_wallet.save()
			# if receive_user:
			transaction = Transaction(send_user = send_user.username, receive_user = receive_user.username,state = True, allow = True, amount = amount, monetary_unit = request.POST['monetary_unit'], created_at = datetime.datetime.now())
			transaction.save()
			return redirect('/wallet/')
		else:
			messages.success(request, ('Receiver wallet is not created'))
			return redirect('/wallet/')

def request(request):
	if request.method == 'POST':
		send_user = request.user
		receive_user = User.objects.get(username = request.POST['receive_user'])
		amount = request.POST['amount']
		transaction = Transaction(send_user = send_user.username, receive_user = receive_user.username,state = True, amount = amount, monetary_unit = request.POST['monetary_unit'], created_at = datetime.datetime.now())
		transaction.save()
		messages.success(request, ('Request is completely send'))
		return redirect('/wallet/')

def accept(request,id):
	trans = Transaction.objects.filter(id = id).values()
	if trans:
		tran = Transaction.objects.get(id = id)
		payer = User.objects.get(username = tran.send_user)
		payer_wallet = Wallet.objects.get(user_id = payer.id)
		payer_wallet.balance = float(payer_wallet.balance) + float(tran.amount)
		receiver = User.objects.get(username = tran.receive_user)
		receiver_wallet = Wallet.objects.get(user_id = receiver.id)
		receiver_wallet.balance = float(receiver_wallet.balance) - float(tran.amount)
		tran.allow = True
		tran.save()
		payer_wallet.save()
		receiver_wallet.save()
	return redirect('/wallet/')
	
def reject(request,id):
	trans = Transaction.objects.filter(id = id).values()
	if trans:
		tran = Transaction.objects.get(id = id)
		tran.state = False
		tran.save()
	return redirect('/wallet/')
	
def re_req(request,id):
	trans = Transaction.objects.filter(id = id).values()
	if trans:
		tran = Transaction.objects.get(id = id)
		tran.state = True
		tran.save()
	return redirect('/wallet/')