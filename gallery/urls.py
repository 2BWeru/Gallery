from django.urls import path

from Main.settings import MEDIA_URL
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    path('',views.navbar,name = 'navbar'),
    path('home/',views.home,name = 'home'),
    path('location/<int:id>',views.locationPage,name = 'image-location'),
    path('category/',views.searchCategory,name = 'search-category'),
    path('type/<int:id>',views.showCategory,name = 'show-category'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
