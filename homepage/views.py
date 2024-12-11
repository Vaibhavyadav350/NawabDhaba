from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from customers import views
from .forms import UserCreateForm
from customers.models import *
# from customers.forms import  CustomerForm




def index(request):
    page = 'login'

    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username = username)
        except:
            print("Username does not exist")
        
        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('loggedin')
        else:
            print("Username or password is incorrect")

    context = {'page':page}
    return render(request, "homepage/index.html",context)

def abbouthome(request):
    page = 'about'
    context = {'page':page}
    return render(request, "homepage/abbout.html",context)

     

@login_required(login_url='login')
def loggedIn(request):
    
    return render(request,"homepage/loggedin.html")

@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

# user = Customer.objects.get(id =pk)
# print(user)

# def feedback(request):
    
#     user = request.user.id
#     required_user = Customer.objects.get(id = user)
#     print(required_user)
#     # form = CustomerFeedbackForm(instance=required_user)
#     # if request.method == 'POST':
#     #     form = CustomerFeedbackForm(request.POST, instance=required_user)
#     #     if form.is_valid():
#     #         form.save()
#     #         messages.success(request, "Your feedback sent successfully. Thank you.")
#     # context = {'form':form}
#     return render(request,"homepage/feedback.html")

def registerUser(request):
    page = 'register'
    
    # Initialize the form
    form = UserCreationForm()

    # Check if the form was submitted (POST request)
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user, no need to call user.save() again
            messages.success(request, 'User account created successfully!')
            return redirect('login')  # Redirect to the login page after successful registration
    
    # Context for rendering
    context = {'page': page, 'form': form}
    return render(request, 'homepage/index.html', context)