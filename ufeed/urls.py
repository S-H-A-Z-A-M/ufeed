from django import views
from django.urls import path
from . import views
from .views import Accept_view

app_name ='ufeed'

urlpatterns = [
    path('',views.home_page,name='home'),
    path('registration/',views.Register_view,name='register'),
    path('contact_info/',views.contact_info, name = 'contact'),
    path('sign_info/',views.login_user,name='sign_in'),
    path('donate/',views.donate_view, name='donate'),
    path('list_of_hotels', views.LOH, name='list'),
    path('accept/<int:pk>/',Accept_view.as_view(),name='delete'),
]