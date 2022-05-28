from turtle import title
from django.test import TestCase
from .models import Imagegallery,Category,Location

# Create your tests here.
class ImagegalleryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.mount_Kenya= Imagegallery(name="mount_Kenya",id=22,description="Holla",image="assets/css/images",web_address="http://assets/css/images")
    def test_instance(self):
        self.assertTrue(isinstance(self.mount_Kenya,Imagegallery))
    # Testing Save Method
    def test_save_method(self):
        self.mount_Kenya.save_imagegallery()
        images= Imagegallery.objects.all()
        self.assertTrue(len(images) > 0)
    
    def test_get_image(self):
        save_imagegallery = Imagegallery.save_imagegallery(self,)
        self.assertTrue(len(save_imagegallery)>0)
    

    def test_get_images_by_id(self):
        test_id= '3'
        id_images = Imagegallery.id_images(id)
        self.assertTrue(len(id_images) == 0)




class LocationTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.ghana= Location(venue="ena",id=22,address="accra",date_created="2012-04-23",)
    def test_instance(self):
        self.assertTrue(isinstance(self.ghana,Location))
    # Testing Save Method
    def test_save_method(self):
        self.ghana.save_Location()
        locations= Location.objects.all()
        self.assertTrue(len(locations) > 0)





class CategoryTestClass(TestCase):
        # Set up method
    def setUp(self):
        self.food= Category(title="matoke",id=2,post_date="2020-02-12")
    def test_instance(self):
        self.assertTrue(isinstance(self.food,Category))
    # Testing Save Method
    def test_save_method(self):
        self.food.save_Category()
        categories= Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def tearDown(self):
        Location.objects.all().delete()
        Category.objects.all().delete()
        Imagegallery.objects.all().delete()

