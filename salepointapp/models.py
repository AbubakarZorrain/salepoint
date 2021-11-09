from unittest import result
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import F


class Product(models.Model):
    name = models.CharField(max_length=80, unique=True)
    quantity = models.IntegerField( null=True)
    scheme = models.IntegerField( null=True)
    rate = models.IntegerField (null=True)
    discountPercent = models.IntegerField( null=True)
    discount = models.IntegerField( null=True)
    gst = models.IntegerField( null=True)
    value = models.IntegerField( null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
            return '{}'.format(self.id)
    def __str__(self):
        return  self.name



class Company(models.Model):
    name = models.CharField(max_length=80, unique=True)
    def __str__(self):
        return  self.name


class Purchase(models.Model):
    name = models.CharField(max_length=80, unique=True)
    quantity = models.IntegerField( null=True)
    scheme = models.IntegerField( null=True)

    discountPercent = models.IntegerField( null=True)
    discount = models.IntegerField( null=True)
    gst = models.IntegerField( null=True)
    value = models.IntegerField( null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateField(auto_now_add=True,null=True)
    Company = models.ForeignKey(Company,on_delete=models.CASCADE, related_name='company')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='users',null=True)
    product = models.ManyToManyField(Product)
    class Meta:
        ordering = ('-date_created',)
    def __str__(self):
        return  self.name
class Routes(models.Model):
    AreaName = models.CharField(max_length=80, unique=True)
    AreaDistance = models.CharField(max_length=80, unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='admins',null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        ordering = ('-date_created',)
    def __str__(self):
        return  self.AreaName
class Employee(models.Model):
    name = models.CharField(max_length=80, unique=True)
    phone = models.CharField(max_length=80, unique=True)
    email = models.EmailField(max_length=80, unique=True)
    HomeAdress = models.CharField(max_length=80, unique=True)
    Area = models.ManyToManyField(Routes)
    Salary = models.CharField(max_length=80, unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='admin1',null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    class Meta:
        ordering = ('-date_created',)
    def __str__(self):
        return  self.name

class SaleProduct(models.Model):
    name = models.ForeignKey(Product,related_name='productName',on_delete=models.CASCADE,null=True)
    quantity = models.IntegerField( null=True)
    scheme = models.IntegerField( null=True)
    rate = models.IntegerField (null=True)
    discountPercent = models.IntegerField( null=True)
    discount = models.IntegerField( null=True)
    gst = models.IntegerField( null=True)
    value = models.IntegerField( null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    product_image = models.ImageField(upload_to='product_image/', null=True, blank=True)
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
            return '{}'.format(self.id)

class sale(models.Model):
    Area = models.ManyToManyField(Routes)
    employee = models.ManyToManyField(Employee)
    products = models.ManyToManyField(Product)
    quantity = models.IntegerField(null=True)
    scheme = models.IntegerField(null=True)
    discountPercent = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    gst = models.IntegerField(null=True)
    value = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='admin2',null=True)
    saleproduct = models.ManyToManyField(SaleProduct,related_name='productforsale')
    class Meta:
        ordering = ('-date_created',)

class OrderItem(models.Model):
    #id = models.ForeignKey(sale.id,on_delete=models.CASCADE, related_name='items',null=True)
    sales = models.ForeignKey(sale,on_delete=models.CASCADE, related_name='items',null=True)

    product = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    size = models.CharField(max_length=100,null=True)

    def __str__(self):
        return '{}'.format(self.id)


