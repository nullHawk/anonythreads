from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.dashboard.as_view(),name='dashboard'),
    path('confess_detail/<int:confession_id>',views.confess_detail.as_view(),name="confess_detail"),\
    path('like/<int:confession_id>/',views.dashboard.as_view(),name='like'),
    path('create_conf/',views.create_conf.as_view(),name="create_conf"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('about/', views.about, name='about'),
    path('profile/',views.profile, name='profile')
]
