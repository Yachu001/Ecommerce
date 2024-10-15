from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Customer

# Create your views here.
def Customer_account(request):
    if request.POST and 'register' in request.POST:
        try:
            username = request.POST.get('name')
            email = request.POST.get('email')
            password  = request.POST.get('password')
            address = request.POST.get('address')
            phone = request.POST.get('phone')

            user =User.objects.create_user(
                username =username,
                password = password,
                email = email
            )

            customer = Customer.objects.create(
                name = username,
                user = user,
                address = address,
                phone = phone,
            )
            print(customer)
            successmsg = 'User Registered Successfully'
            messages.success(request,successmsg)

        except Exception as e:
            error_messages = ' Duplicate username  '
            messages.error(request,error_messages)
           
    
    if request.POST and 'login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user =authenticate(username = username,password = password)
        if user:
            login(request,user)
            messages.success(request, 'login successful')
            return redirect('home')
        else:
            e_messages = 'Invalid user credential'
            messages.error(request,e_messages)

    return render(request, 'account.html')

def Logout_view(request):
    logout(request)
    return redirect('home')