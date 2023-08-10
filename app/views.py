from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['user_password']

        #authenticate
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"you have been successfully logged in,Good day!")
            return redirect('home')
        else:
            messages.success(request,'There was an error while logging in ...please try again!')
            return redirect('home')

    else:        
        return render(request,'home.html' ,{})
    

def logout_user(request):
    logout(request)
    messages.success(request,'you have been logged out from the system...')
    return redirect('home')


def register_user(request):
    

    return render(request,'register.html',{})
