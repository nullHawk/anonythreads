from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Confession
from .forms import ConfessionForm
from datetime import datetime
from django.shortcuts import render, get_object_or_404

# Create your views here.


class dashboard(View):
    template_name = 'dashboard/dashboard.html'
    paginate_by = 20  # Set the number of items per page

    def get(self, request):
        if request.user.is_authenticated:
            confession_list = Confession.objects.all()

            # Create a paginator instance
            paginator = Paginator(confession_list, self.paginate_by)

            # Get the current page number from the request's GET parameters
            page = request.GET.get('page')

            try:
                # Get the Page object for the requested page
                confessions = paginator.page(page)
            except PageNotAnInteger:
                # If the page parameter is not an integer, deliver the first page
                confessions = paginator.page(1)
            except EmptyPage:
                # If the page is out of range (e.g., 9999), deliver the last page
                confessions = paginator.page(paginator.num_pages)

            return render(request, self.template_name, {'confessions': confessions})
        else:
            return HttpResponse("Unauthorized Access")

    def post(self, request, confession_id):
        action = request.POST.get('action')
        confession = Confession.objects.get(pk=confession_id)
        
        if action == 'like':
            if request.user not in confession.likes_users.all():
                # User has not liked before
                confession.likes_users.add(request.user)
                confession.likes += 1
                confession.save()
        elif action == 'dislike':
            if request.user not in confession.dislikes_users.all():
                # User has not disliked before
                confession.dislikes_users.add(request.user)
                confession.dislikes += 1
                confession.save()
        
        confession.save()

        # Redirect to the current page with the pagination
        return redirect("dashboard")
   

        

class create_conf(View):
    def get(self, request):
        user = request.user
        form = ConfessionForm()
        return render(request, 'dashboard/create_confess.html',{'user':user, 'form':form})
    
    def post(self, request):
        form = ConfessionForm(request.POST)
        if form.is_valid():
            # Save the confession and do any additional processing
            confession = form.save(commit=False)
            confession.user = request.user  # Set the user (assuming you have a user model)
            confession.pub_date = datetime.now()
            confession.save()
            return redirect('dashboard')
        else:
            HttpResponse("Error Occured")

class confess_detail(View):
    def post(self,request, confession_id):
        action = request.POST.get('action')
        confession = Confession.objects.get(pk=confession_id)
        
        if action == 'like':
            if request.user not in confession.likes_users.all():
                # User has not liked before
                confession.likes_users.add(request.user)
                confession.likes += 1
                confession.save()
        elif action == 'dislike':
            if request.user not in confession.dislikes_users.all():
                # User has not disliked before
                confession.dislikes_users.add(request.user)
                confession.dislikes += 1
                confession.save()
        
        confession.save()

        return redirect(reverse('confess_detail', kwargs={'confession_id': confession_id}))
    def get(self, request, confession_id):
        if request.user.is_authenticated:
            confession = get_object_or_404(Confession, pk=confession_id)
            return render(request, 'dashboard/detail_confess.html',{'confession':confession})
        else:
            return HttpResponse("Unauthorized Acess")

def about(request):
    return render(request, 'dashboard/about.html')

def profile(request):
    user = request.user

    user_posts = Confession.objects.filter(user=user)

    context = {'user_posts': user_posts}
    return render(request, 'dashboard/profile.html', context)