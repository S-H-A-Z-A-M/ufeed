from ast import Pass
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from . import models
from .models import donate
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import *
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print("shazam")
                return redirect(reverse('ufeed:home'))
    return render(request, 'ufeed/sign_in.html')    


def Register_view(request):
    print(request.POST)
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        contact = request.POST['contact']
        user = User.objects.create_user(username=email,password=password,first_name=name)
        return redirect(reverse('ufeed:sign_in'))
    else:
        return render(request,'ufeed/Registration_form.html')

@login_required(login_url="ufeed:sign_in")
def contact_info(request):
    print(request.POST)
    if request.POST:
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        prob = models.problem.objects.create(name=name, email=email,subject=subject,message=message)
        send_mail(
            subject="Your Query has been Received",
            message=f"HI,{prob.name}"
            f"We have received your query and our team will respond to it as early as possible",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[prob.email]
        )
        return redirect(reverse('ufeed:sign_in'))
    else:    
        return render(request,'ufeed/contact_info.html')

def home_page(request):
    return render(request, 'ufeed/home_page.html')

@login_required(login_url="ufeed:sign_in")
def donate_view(request):
        if request.POST:
            name = request.POST['name']
            contact = request.POST['contact']
            address = request.POST['address']
            amount = request.POST['amount']
            models.donate.objects.create(name=name, contact=contact,address=address, amount=amount)
            return redirect(reverse('ufeed:list'))
        else:
            return render(request, 'ufeed/donate.html')        

def LOH(request):
    un_data = donate.objects.all()
    data = un_data[::-1]
    return render(request, 'ufeed/LOH.html', {'data':data})     

class Accept_view(DeleteView):
    # Requires model_confirm_delete.html template name
    model = donate
    
    success_url = reverse_lazy('ufeed:home')
    