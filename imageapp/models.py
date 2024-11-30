from django.db import models

# Create your models here.
class person(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    def __str__(self):
        return self.first_name

class FAQ(models.Model):
    ques=models.TextField()
    ans=models.TextField()
    def __str__(self):
        return self.ques 
    
class myreview(models.Model):
    title=models.CharField(max_length=1000)
    message=models.TextField()
    def __str__(self):
        return self.title 
    
class Help(models.Model):
    title=models.CharField(max_length=1000)
    message=models.TextField()
    def __str__(self):
        return self.title

class contactme(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    message=models.TextField()
    def __str__(self):
        return self.email
    
class register(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=20)
    phoneno=models.CharField(max_length=13 ,blank=True ,null=True)
    Country=models.CharField(max_length=50 ,blank=True ,null=True)
    State=models.CharField(max_length=50 ,blank=True ,null=True)
    Address=models.CharField(max_length=100 ,blank=True ,null=True)
    Pincode=models.CharField(max_length=100 ,blank=True ,null=True)
    detail=models.CharField(max_length=500 ,blank=True ,null=True) 
    profile=models.ImageField(upload_to="data",blank=True, null=True)
    def __str__(self):
        return self.email
    
class article(models.Model):
    title=models.CharField(max_length=1000)
    description=models.TextField()
    Image=models.ImageField(upload_to="data", default=None)
    Writter=models.CharField(max_length=1000)
    def __str__(self):
        return self.title
    
class editor(models.Model):
    Image=models.ImageField()
    name=models.CharField(max_length=1000)
    description=models.TextField
    Website=models.CharField(max_length=1000)
    def __str__(self):
        return self.name   

