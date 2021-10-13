
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(requests):
    return render(requests,"authentication/signin.html")


def afterlogin(request):
    return render(request,"authentication/index.html")


def signup(request):
    if request.method =='POST':
        #username=requests.POST.get('username')
        username=request.POST['username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']

        message=""
        if User.objects.filter(username=username):
            messages.error(request,"Username already exists")
            # return redirect('home')
            message="Username already exists"
            return render(request,'authentication/signup.html',{'message':message})
        if User.objects.filter(email=email):
            messages.error(request,"Email already exists")
            # return redirect('home')
            message="Email already exists"
            return render(request,'authentication/signup.html',{'message':message})

        if password!=cpassword:
            messages.error(request,"Password didn't matched")
            # return redirect('home')
            message="Password didn't matched"
            return render(request,'authentication/signup.html',{'message':message})


        myuser=User.objects.create_user(username,email,password)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,'Your account has been successfully created')
        return redirect("home")

    return render(request,"authentication/signup.html")

def signin(request):
    if request.method =='POST':
        user=request.POST['username']
        pass1=request.POST['password']

        user = authenticate(username=user ,password=pass1)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'authentication/index.html',{'fname':fname})
            #return redirect('afterlogin')
            # return render(request,"authentication/index.html",{'fname':fname})
        else:
            # messages.error(request,"BAD Credentials")
            # return redirect('home')
            message="Invalid Username or password"
            return render(request,'authentication/signin.html',{'message':message})
    return render(request,"authentication/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('home')

def base(request):
    return render(request,'authentication/base.html')