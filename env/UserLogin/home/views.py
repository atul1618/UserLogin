from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Create your views here.


class Home(TemplateView):
    model=User
    template_name = "home/home_page.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(Home, self).dispatch(request,*args, **kwargs)
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name)


class UserDetails(TemplateView):
    model=User
    template_name = "home/profile.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(UserDetails, self).dispatch(request,*args,*kwargs)
    def get(self, request, *args, **kwargs):
        qs = User.objects.filter(username=request.user)
        context = {'userdetails': qs}
        return render(request, self.template_name, context)

