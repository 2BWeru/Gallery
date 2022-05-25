from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.navbar,name = 'navbar'),
    url('home/',views.home,name = 'home'),
]
