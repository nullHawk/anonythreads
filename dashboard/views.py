from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.views import View
from .models import Confession

# Create your views here.
class dashboard(View):
    def get(self, request):
        if request.user.is_authenticated:
            confessions = Confession.objects.all()
            return render(request, 'dashboard/dashboard.html',{'confessions':confessions})
        else:
            return HttpResponse("Unauthorized Acess")
        

