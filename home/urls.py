from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home.as_view(),name='home'),
    path('signup',views.signup,name='signup')
]
