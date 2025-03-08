from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, SignInForm
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, "index.html",{
        'products':products
    })   


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin_view(request):
    if request.method == "POST":
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = SignInForm()
    return render(request, 'signin.html', {'form': form})

def signout_view(request):
    logout(request)
    return redirect('signin')

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})
    
    

def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {'products': products})

def product(request, product_id: int):
    product = Product.objects.get(id=product_id)
    return render(request, "product.html", {"product": product})

def card(requst):
    pass

def add_to_card(requst,product_id:int):
    pass