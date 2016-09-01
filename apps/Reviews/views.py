from django.shortcuts import render, HttpResponse, redirect

import bcrypt, re
from django.contrib import messages
# Create your views here.
def index(request):
	products = items.objects.all()
	context = {'products' : products}
	return render(request, 'Day_8_Routes/index.html', context)

def show(request, item_id):
	products = items.objects.all().filter(id= item_id)
	context = {'products' : products}
	return render(request, 'Day_8_Routes/show.html', context)

def new(request):
	return render(request, 'Day_8_Routes/new.html')

def create(request):
	name = request.POST['name']
	desc = request.POST['desc']
	price = request.POST['price']
	items.objects.create(name=name,description=desc,price=price)
	return redirect('/')

def edit(request, item_id):
	products = items.objects.all().filter(id= item_id)
	context = {'products' : products}
	return render(request, 'Day_8_Routes/edit.html', context)

def update(request, item_id):
	name = request.POST['name']
	desc = request.POST['desc']
	price = request.POST['price']
	items.objects.update(name=name,description=desc,price=price)
	return redirect('/')

def destroy(request, item_id):
	products = items.objects.all().filter(id= item_id).delete()
	return redirect('/')