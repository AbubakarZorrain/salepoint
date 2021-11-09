from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import re_path

urlpatterns = [
    path('purchases',views.purchases,name="purchases"),
    path('sales/',views.sales),
    path('employee',views.employee),
    path('products',views.products),
    path('saleProduct',views.saleProduct),
    path('routes',views.routes),
    path('',views.home)

]