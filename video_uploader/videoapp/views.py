from django.shortcuts import render,HttpResponseRedirect
from .models import Video
from .forms import Newform,Fistform

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
# Create your views here.

# Create your views here.

def first(request):
    video = Video.objects.all()
    return render(request,'videoapp/first.html',{'video':video})



def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = Newform(request.POST,request.FILES)
            if fm.is_valid():
                fm.save()
        
        form = Newform()
        video = Video.objects.all()
        return render(request,'videoapp/home.html',{'video':video,'form':form})
    else:
        return HttpResponseRedirect('/login/')





def home2(request):
    if request.method == 'POST':
        fm = Fistform(request.POST)
        if fm.is_valid():
            messages.info(request,'you have been signed in successfully , ')
            fm.save()
            return HttpResponseRedirect('/login/')
    else:
        fm = Fistform()
    return render(request,'videoapp/home2.html',{'form':fm})

def user_login(request):
        if request.method == 'POST':
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username = uname , password = upass)
                if user is not None:
                    login(request, user)
                    messages.info(request,'you have been login in successfully,')
                    return HttpResponseRedirect('/home/')
        else:
            fm = AuthenticationForm()
        return render(request,'videoapp/login.html',{'form':fm})
    
    
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def delete(request, stu):
    if request.method == 'POST':
        pi = Video.objects.get(id=stu)
        pi.delete()
        return HttpResponseRedirect('/home/')