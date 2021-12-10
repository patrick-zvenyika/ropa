from django.urls import path
from . import views
from django.conf.urls import url 

urlpatterns = [
    path('home', views.home, name = 'index' ),
    path('', views.register, name ='signup'),
    path('/inbox', views.inbox, name = 'inbox'),
    path('profile', views.profile, name = 'profile'),
    path('/groups', views.groups, name= 'groups'),
    path('chart', views.chart, name = 'chart')
]