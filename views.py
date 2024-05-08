from django.shortcuts import render, redirect
from ChitChat.form import ChatAppForm
from django.contrib import messages
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    return render(request, "chat/chatPage.html", context)



@login_required(login_url="/login/")
def signout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("login")


def loginVW(request):
  if request.user.is_authenticated:
    return redirect("chat")
  else:
    if request.method=='POST':
       name=request.POST.get('username')
       pwd=request.POST.get('password')
       user=authenticate(request,username=name,password=pwd)
       if user is not None:
          login(request,user)
          messages.success(request,"Logged in Successfully")
          return redirect("chat")
       else:
          messages.error(request,"Invalid User Name or Password")
          return redirect("login")   
    return render(request,"chat/loginPage.html")




def registerVW(request):
    form=ChatAppForm()
    if request.method=='POST':
        form=ChatAppForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You can Login Now..!")
            return redirect('/login')
    return render(request,'chat/register.html',{'form':form})

