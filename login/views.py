from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def contact(request):
    return render(request, "contact.html")

def listing(request):
    return render(request, "listings.html")

def login(request):
    return render(request, "login.html")

def registerP(request):
    return render(request, "register.html")

def search(request):
    return render(request, "search.html")

def view_property(request):
    return render(request, "view_property.html")

# views.py

from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['pass']
        c_password = request.POST['c_pass']

        if password != c_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        print(password)
        print(c_password)
        print(email)
        print(name)
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        else:
            # Create user
            user = User.objects.create(name=name, email=email, password=password)
            user.save()
            messages.success(request, "You are now registered and can log in")
            print("after")
            print(password)
            print(c_password)
            print(email)
            print(name)
            return redirect('login')
    else:
        return render(request, 'register.html')


def validateUser(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['pass']

        try:
            user = User.objects.get(email=email)
            # print(user)
            if user.password == password:
                # Authentication successful, redirect to some page
                # For example, redirect to the home page
                return redirect('home')
            else:
                # Password incorrect
                messages.error(request, "Invalid email or password")
                return redirect('login')
        except User.DoesNotExist:
            # User does not exist
            messages.error(request, "Invalid email or password")
            return redirect('login')
    else:
        # If it's not a POST request, redirect to the login page
        return redirect('login')