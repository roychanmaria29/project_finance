from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('customer')
        else:
            messages.info(request,"Invalid")
            return redirect("login")

    return render(request,"login.html")



def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['psw']
        cpassword = request.POST['psw-repeat']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already taken")
                return redirect('/')
            else:
                user = User.objects.create_user(username=username,password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request,"Please check your password")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')

def customer(request):
    # return redirect('/')
    return render(request,"customer.html")

def home(request):
    return render(request,"index.html")


