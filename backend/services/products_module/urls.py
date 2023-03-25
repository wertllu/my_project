from django.urls import path, include
from services.products_module.views import get_my_products
from services.products_module.views import index, myinit, mytest


urlpatterns = [
    path('',index, name='index'),
    path('myinit', myinit, name='myinit'),
    path('mytest', mytest, name='mytest'),

    path('my_products/', get_my_products, name='my_products'),
    path('product/', get_my_products, name='my_product'),
]

