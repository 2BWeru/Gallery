from datetime import timezone
from distutils.command import upload
from email.headerregistry import Address
from turtle import title
from unicodedata import category
from uuid import uuid4
from django.template.defaultfilters import slugify
# from django_resized import ResizedImageField
from django.db import models
from django.urls import reverse

# Create your models here.
class Location(models.Model):
    venue = models.CharField(null=True, blank=True, max_length=100)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    address=models.CharField(null=True, blank=True, max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.venue

    def save_Location(self):
        self.save()


class Category(models.Model):
    title = models.CharField(max_length=100)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    
    
    
    def __str__(self):
        return self.title

    def save_category(self):
        self.save()

    
    @classmethod
    def search_by_title(cls,searched_term):
        category = cls.objects.filter(title__icontains=searched_term)
        return category
    

class Imagegallery(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    description = models.TextField(max_length=100)
    date_created = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')
    web_address=models.FilePathField(null=True, blank=True, max_length=100,unique=True)
    hashtags = models.CharField(null=True, blank=True, max_length=100)
    location = models.ForeignKey(Location,null=True, blank=True,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,null=True, blank=True,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name

    #  save
    def save_imagegallery(self):
        self.save()



