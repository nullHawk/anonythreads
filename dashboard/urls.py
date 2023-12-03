from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.dashboard.as_view(),name='dashboard'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
