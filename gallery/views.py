from turtle import title
from unicodedata import category, name
from urllib import request
from xml.sax.xmlreader import Locator
from django.http import Http404, HttpRequest
from django.shortcuts import render
from .models import Category, Imagegallery, Location

# Create your views here.
def navbar(request):

    return render(request,'navbar.html')

def home(request):
    locations = Location.objects.all()
    

    context = {}
    context['locations'] = locations

    return render(request,'home.html',context)

def locationPage(request,id):
    try:
        locations = Location.objects.get(id=id)
        images = Imagegallery.objects.filter(location=locations)
        # for x in images:
        #   x.shortDescription = x.description[:130]
        context = {}
        context['images'] = images
        context['locations'] = locations

    except:
        ValueError
        raise 'Error'

    return render(request, 'main/location.html', context)


def searchCategory(request):
    if "category" in request.GET and request.GET["category"]:
        searched_item=request.GET["category"]
        categories= Category.search_by_title(searched_item)
        message = f"{searched_item}"


        return render(request, 'main/search.html',{"message":message,"categories":categories})
    else:
        message = "Kindly input a search term to get any results"
        return render(request, 'main/search.html',{"message":message})

def showCategory(request,id):
    try:
        categories = Category.objects.get(id=id)
        images = Imagegallery.objects.filter(category=categories)
       
        context = {}
        context['images'] = images
        context['categories'] = categories
    except:
        ValueError
        raise 'Error'
    return render(request, "main/show-category.html",context)
