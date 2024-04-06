from django.db import models
from django.contrib.auth.models import User


class Categories(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255)

class Customers(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Brands(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=255)
class Stores(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)


class Staffs(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    store_id = models.ForeignKey(Stores, on_delete=models.CASCADE)
    manager_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)


class Orders(models.Model):
    PENDING = 1
    PROCESSING = 2
    REJECTED = 3
    COMPLETED = 4

    order_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customers, on_delete=models.CASCADE)
    order_status = models.IntegerField(choices=[
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (REJECTED, 'Rejected'),
        (COMPLETED, 'Completed')
    ])
    order_date = models.DateField()
    required_date = models.DateField()
    shipped_date = models.DateField(null=True, blank=True)
    store_id = models.ForeignKey(Stores, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Staffs, on_delete=models.CASCADE)

class Products(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    brand_id = models.ForeignKey(Brands, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)
    model_year = models.SmallIntegerField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2)

class Order_Items(models.Model):
    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    item_id = models.IntegerField()
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    last_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    class Meta:
        unique_together = ('order_id', 'item_id')

class Stocks(models.Model):
    store_id = models.ForeignKey(Stores, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('store_id', 'product_id')

