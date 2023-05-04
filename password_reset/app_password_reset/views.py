from django.shortcuts import render, redirect,HttpResponse
from  django.http import HttpResponse
from django.views import View

from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import login, logout
from django.contrib import messages

# Create your views here.
def Home(request):
    
    return render(request, 'master.html')

class Login(View):
    def get(self, request):

        return render(request, 'login.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        check = request.POST['check']

        user = auth.authenticate(request, username=username,password=password,check=check)

        if user:
            login(request,user)
            messages.success(request, 'Login Successfully.')
            return redirect('/')
        else:
            messages.error(request, 'Invalid username or password.')
        return redirect('login')

class Register(View):
    def get(self,request):
        return render(request, 'register.html')
    
    def post(self,request):
        first_name= request.POST['first_name']
        last_name=request.POST['last_name']
        email= request.POST['email']
        username=request.POST['username']
        password= request.POST['password']
        try:
            user =  User.objects.get(username=username)
            if user:
                messages.error(request, 'Username Already Exists. Try with new  one.')
                return redirect('registration')
        except:
            data=User.objects.create_user(first_name=first_name, last_name=last_name,email=email,username=username,password=password)
            data.save()
            messages.success(request, 'Account has been created successfully!')

        return redirect('login')

class Logout(View):
    def get(self,request):
        logout(request)

        messages.success(request, "You're Logged Out !!")
        return redirect('login')