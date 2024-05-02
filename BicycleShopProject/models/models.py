from django.db import models
from django.contrib.auth.models import AbstractUser


class Categorie(models.Model):
    category_id = models.AutoField(primary_key=True, db_column='category_id')
    category_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'categories'

class Brand(models.Model):
    brand_id = models.AutoField(primary_key=True, db_column='brand_id')
    brand_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'brands'

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True, db_column='user_id')
    phone = models.CharField(max_length=255, blank=True, null=True)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, db_column='manager_id')

    class Meta:
        db_table = 'users'

class Order(models.Model):

    PENDING = 1
    PROCESSING = 2
    REJECTED = 3
    COMPLETED = 4
    DRAFT = 5

    order_id = models.AutoField(primary_key=True, db_column='order_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column='user_id', related_name='order_user')
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
    staff = models.ForeignKey(User, null=True, on_delete=models.CASCADE, db_column='staff_id', related_name='order_staff')

    class Meta:
        db_table = 'orders'

class Product(models.Model):
    product_id = models.AutoField(primary_key=True, db_column='product_id')
    product_name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, db_column='brand_id')
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE, db_column='category_id')
    model_year = models.SmallIntegerField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'

class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True, db_column='order_item_id')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    quantity = models.IntegerField()
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=4, decimal_places=2, default=0)

    class Meta:
        db_table = 'order_items'

class Stock(models.Model):
    stock_id = models.AutoField(primary_key=True, db_column='stock_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    quantity = models.IntegerField()

    class Meta:
        db_table = 'stocks'

