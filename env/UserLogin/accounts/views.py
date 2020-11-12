from django.shortcuts import render,redirect
from django.views.generic import  TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .forms import UserForm
# Create your views here.


class UserRegistration(TemplateView):
    model=User
    template_name = "accounts/user_register.html"
    form_class=UserForm

    def get(self, request, *args, **kwargs):
        form=self.form_class
        context={'form':form}
        return render(request,self.template_name,context)

    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            print("Valid")
            form.save()
            return redirect('login')
        else:
            form=self.form_class(request.POST)
            context={'form':form}
            return render(request,self.template_name,context)


class UserLogin(TemplateView):
    model=User
    template_name = "accounts/user_login.html"

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)

    def post(self,request,*args,**kwargs):
        userid=request.POST.get('username')
        pwd=request.POST.get('password')
        user=authenticate(request,username=userid,password=pwd)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            msg='Incorrect password or username'
            context={'message':msg}
            return render(request,self.template_name,context)


def userlogout(request):
    logout(request)
    return redirect('login')


