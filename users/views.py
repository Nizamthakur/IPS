from django.shortcuts import render
from django.http import HttpResponseRedirect 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import RegisterForm
# Create your views here.
def register (request): 
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, Your account is created!')
            return HttpResponseRedirect ('/login/')
    else:
        form = RegisterForm()
    return render (request, 'register.html',{'form':form})
@login_required
def profilepage(request):
    return render (request, 'profile.html')