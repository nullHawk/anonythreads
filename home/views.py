from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import SignUpForm
from django.views import generic

# Create your views here.

class home(View):
    def get(self,request):
        return render(request,'home/home.html')

    def post(self,request):
        username = request.POST.get('username')
        pwd = request.POST.get('password')
        user = authenticate(request,username=username, password=pwd)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Username password is incorrect")
        return render(request,'home/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'home/signup.html', {'form': form})


