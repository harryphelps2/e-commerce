from django.conf.urls import url, include, re_path
from .views import all_products

urlpatterns = [
    re_path(r'^$', all_products, name='products')
]
