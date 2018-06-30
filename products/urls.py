from django.conf import settings
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


app_name = 'products'

urlpatterns = [
    
    url(r'getProducts/$', views.GetProducts.as_view(), name='GetProducts'),
    
    ]
