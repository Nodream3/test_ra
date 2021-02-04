from django.urls import path
from django.conf.urls import include
from . import views

app_name = 'test1'

urlpatterns = [
    path('', views.test1, name='test1'),
    path('forms/', views.form_name_view, name='forms'),
    path('data_list/', views.data_list, name='data_list'),
    path('runAPI/', views.runAPI, name='runAPI'),
    path('friend_list/', views.friend_list, name='friend_list'),

]
