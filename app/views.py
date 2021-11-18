from django.shortcuts import render,redirect
from .models import *
from django.core.mail import send_mail

def index(request):
    data=Line.objects.all()
    dev=Team.objects.all()
    about=About.objects.all().last()
    service=Service.objects.all()
    pro=Project.objects.all()
    client=Client.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        msg=request.POST['msg']
        send_mail(
            'Bhakti WebTech',
            'We received you mail. We will revert you as soon as possible. It will take some time for us to reply. Thank you for waiting',
            'bhaktiwebtech20@gmail.com',
            [email],
        )
        Contact(name=name,email=email,subject=subject,msg=msg).save()
    return render(request,'index.html',{'data':data,'dev':dev,'about':about,'service':service,'pro':pro,'client':client})

def detail(request):
    pid=request.GET.get('pid')
    prod=Project.objects.get(pk=pid)
    return render(request,'portfolio-details.html',{'prod':prod})