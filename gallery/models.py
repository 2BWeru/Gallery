from datetime import datetime
from django.db import models

# Create your models here.
class Location(models.Model):
    venue = models.CharField(null=True, blank=True, max_length=100)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    address=models.CharField(null=True, blank=True, max_length=100)
    date_created = models.DateTimeField(auto_now_add=True,blank=True, null=True)


    def save_Location(self):
        self.save()
    
    def delete_location(self): 
        self.delete() 
    
    def __str__(self):
        return self.venue


class Category(models.Model):
    title = models.CharField(max_length=100)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    
    
    def save_category(self):
        self.save()

    def delete_location(self): 
        self.delete()

    @classmethod
    def search_by_title(cls,searched_term):
        category = cls.objects.filter(title__icontains=searched_term)
        return category
    
    def __str__(self):
        return self.title




class Pictures(models.Model):
    name = models.CharField(max_length=50)
    id = models.CharField(max_length=50,primary_key=True, unique=True, blank=True)
    description = models.TextField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    image = models.ImageField(upload_to='pics/')
    hashtags = models.CharField(null=True, blank=True, max_length=100)
    location = models.ForeignKey(Location,null=True, blank=True,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,null=True, blank=True,on_delete=models.CASCADE)
    
    #  save
    def save_imagegallery(self):
        self.save()
    
    def delete_location(self): 
        self.delete()


    def __str__(self):
        return self.name

    @classmethod
    def all_images(cls): 
        images= Pictures.objects.all() 
        return images
    
    @classmethod
    def update_image(cls,current_img,new_img):
        updated_img = Pictures.objects.filter(image_name=current_img).update(name=new_img)
        return updated_img

    
