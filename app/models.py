from django.db import models

class About(models.Model):
    disc1=models.TextField()
    disc2=models.TextField()
    disc3=models.TextField()

class Team(models.Model):
    image=models.ImageField(upload_to='img')
    name=models.CharField(max_length=200)
    profile=models.CharField(max_length=200)


class Line(models.Model):
    line=models.CharField(max_length=500)

class Service(models.Model):
    icon=models.ImageField(upload_to='service')
    title=models.CharField(max_length=500)
    desc=models.TextField()

class Project(models.Model):
    img1=models.ImageField(upload_to='pimage')
    img2=models.ImageField(upload_to='pimage')
    img3=models.ImageField(upload_to='pimage')
    p_name=models.CharField(max_length=500)
    p_type=models.CharField(max_length=500)
    p_lang=models.CharField(max_length=500)
    p_url=models.CharField(max_length=200)
    p_disc=models.TextField()

class Contact(models.Model):
    name=models.CharField(max_length=500)
    email=models.EmailField()
    subject=models.CharField(max_length=1000)
    msg=models.TextField()
    
class Client(models.Model):
    name=models.CharField(max_length=500)
    image=models.ImageField(upload_to='client')