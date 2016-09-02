from django.shortcuts import render, HttpResponse, redirect
from .models import users, reviews, books
import bcrypt, re
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
	return render(request, 'Reviews/index.html')

def login(request):
	email = request.POST['email']
	password = request.POST['password'].encode()
	user = users.objects.all().filter(email= email)
	hashed = bcrypt.hashpw(password, bcrypt.gensalt())
	if not user:
		messages.warning(request,"Invalid email")
		return redirect('/')
	else:
		if bcrypt.hashpw(password, hashed) == hashed:
			request.session['logged_in'] = True
			request.session['user_id'] = request.POST['email']
			return redirect('/books')
		else:
			messages.warning(request,"Incorrect password!")
			return redirect('/')
	

def register(request):
	from django.core.validators import validate_email
	from django.core.exceptions import ValidationError
	_digits = re.compile('\d')
	def contains_digits(d):
		return bool(_digits.search(d))
	if len(request.POST['name']) < 2:
		messages.warning(request,"Name must have at least 2 characters!")
		return redirect('/')
	elif contains_digits(request.POST['name']):
		messages.warning(request,"Name may only contain letters")
		return redirect('/')
	else:
		pass

	if len(request.POST['alias']) < 2:
		messages.warning(request,"Alias must have at least 2 characters!")
		return redirect('/')
	else:
		pass

	try:
		validate_email(request.POST['email'])
		valid_email = True
	except ValidationError:
		valid_email = False
	if valid_email != True:
		messages.warning(request, 'Email is not valid')
		return redirect('/')
	elif users.objects.filter(email=request.POST['email']).exists():
		messages.warning(request,"Email already exists")
		return redirect('/')
	else:
		pass

	if len(request.POST['password']) < 8:
		messages.warning(request,"Password must be at least 8 characters!")
		return redirect('/')
	else:
		pass

	if request.POST['confirm_password'] != request.POST['password']:
		messages.warning(request,"Your passwords do not match!")
		return redirect('/')
	else:
		password = request.POST['password'].encode()
		pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())
		first_name1 = request.POST['name']
		last_name1 = request.POST['alias']
		email1 = request.POST['email']
		users.objects.create(name=first_name1, alias=last_name1, email=email1, password=pw_hash)
		request.session['logged_in'] = True
		request.session['user_id'] = request.POST['email']
		return redirect('/books')

def home(request):
	context = {
        'users' : users.objects.all().filter(email=request.session['user_id']),
        'reviews' : reviews.objects.all().prefetch_related('user_id').prefetch_related('book_id')
    }
	return render(request, 'Reviews/home.html', context)

def add(request):
	info = books.objects.all()
	context = {'info' : info}
	return render(request, 'Reviews/add.html', context)

def create(request):
	if books.objects.filter(title=request.POST['title']).exists():
		messages.warning(request,"Book already exists")
		return redirect('/books/add')
	if books.objects.filter(author=request.POST['author']).exists():
		messages.warning(request,"Author already exists. Please choose from the list.")
		return redirect('/books/add')
	else:
		pass
	title = request.POST['title']
	author = request.POST['author']
	books.objects.update(title=title,author=author)
	books_id = books.objects.latest['id']
	review = request.POST['review']
	rating = request.POST['rating']
	users_id = users.objects.filter(email=request.session['user_id']).get('id')
	reviews.objects.update(review=review,rating=rating,book_id=books_id,user_id=users_id)
	review_id = reviews.objects.latest['id']
	return redirect(reverse('views.show', kwargs={'item_id': review_id }))

def show(request, item_id):
	context = {
        'books' : books.objects.all().filter(id=item_id),
        'reviews' : reviews.objects.all().filter(book_id=item_id).prefetch_related('user_id')
    }
	return render(request, 'Reviews/show.html', context)

def review(request, item_id):
	review = request.POST['review']
	rating = request.POST['rating']
	users_id = users.objects.filter(email=request.session['user_id']).get('id')
	reviews.objects.create(review=review,rating=rating,user_id=users_id,book_id=item_id)
	return redirect(reverse('views.show', kwargs={'item_id': item_id }))

def user(request, user_id):
	context = {
        'user' : users.objects.all().filter(id=user_id),
        'reviews' : reviews.objects.all().filter(user_id=user_id).prefetch_related('book_id')
    }
	return render(request, 'Reviews/user.html', context)



