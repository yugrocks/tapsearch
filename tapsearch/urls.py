from django.urls import path
from tapsearch.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('clear_index/', clear_index,name="clear_index"),
    path('search/', search,name="search"),
    path('index_document/', index_document,name="index_document"),
    path('', get_main_page,name="get_main_page"),
    path('get_index_page/', get_index_page,name="get_index_page"),
    path('image_search/', image_search,name="image_search"),
    path('image_search_page/', image_search_page,name="image_search_page"),
    path('index_images/', index_images,name="index_images"),
    path('upload_pdf/', upload_pdf,name="upload_pdf")
    
] 


if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
