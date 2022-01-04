from django.db import models

# Create your models here.
class Angel(models.Model):
    name= models.CharField(max_length=40)
    place= models.CharField(max_length=40)
    serving= models.CharField(max_length=40)  
    

class Cod(models.Model):
    name = models.CharField(max_length=10)
    learn = models.CharField(max_length=50)
    design = models.CharField(max_length=20)

class Animal(models.Model):
    type = models.CharField(max_length=40)
    color = models.CharField(max_length=40)
    breed = models.CharField(max_length=50) 

class Male(models.Model):
    fit = models.CharField(max_length=40) 

class Female(models.Model):  
    fit = models.CharField(max_length=40) 

class Robot(models.Model): 
    full = models.CharField(max_length=40) 
    man = models.CharField(max_length=40)
    sem = models.CharField(max_length=40)

class Ch(models.Model):
    cel = models.CharField(max_length=40) 
    wish = models.CharField(max_length=50)
    tq = models.CharField(max_length=40) 

class Bike(models.Model):
    brand = models.CharField(max_length=40) 
    ver = models.CharField(max_length=40) 

