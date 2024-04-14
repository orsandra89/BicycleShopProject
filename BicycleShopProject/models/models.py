from django.db import models
from django.contrib.auth.models import User


class Categorie(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=255)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'customers'
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Brand(models.Model):
    brand_id = models.IntegerField(primary_key=True)
    brand_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'brands'
class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    store_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    street = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=25, blank=True, null=True)
    zip_code = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        db_table = 'stores'

class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True, db_column='staff_id')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    active = models.IntegerField()
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='store_id')
    manager_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, db_column='manager_id')

    class Meta:
        db_table = 'staffs'

class Order(models.Model):
    PENDING = 1
    PROCESSING = 2
    REJECTED = 3
    COMPLETED = 4
    DRAFT = 5

    order_id = models.IntegerField(primary_key=True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='customer_id')
    order_status = models.IntegerField(choices=[
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (REJECTED, 'Rejected'),
        (COMPLETED, 'Completed'),
        (DRAFT, 'Draft')
    ])
    order_date = models.DateField()
    required_date = models.DateField(null=True, blank=True)
    shipped_date = models.DateField(null=True, blank=True)
    store_id = models.ForeignKey(Store, null=True, on_delete=models.CASCADE, db_column='store_id')
    staff_id = models.ForeignKey(Staff, null=True, on_delete=models.CASCADE, db_column='staff_id')

    class Meta:
        db_table = 'orders'

class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_name = models.CharField(max_length=255)
    brand_id = models.ForeignKey(Brand, on_delete=models.CASCADE, db_column='brand_id')
    category_id = models.ForeignKey(Categorie, on_delete=models.CASCADE, db_column='category_id')
    model_year = models.SmallIntegerField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'

class OrderItem(models.Model):
    order_item_id = models.IntegerField(primary_key=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id')
    item_id = models.IntegerField()
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    quantity = models.IntegerField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    class Meta:
        db_table = 'order_items'

class Stock(models.Model):
    stock_id = models.IntegerField(primary_key=True, auto_created=True)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='store_id')
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    quantity = models.IntegerField()

    class Meta:
        unique_together = ('store_id', 'product_id')
        db_table = 'stocks'

