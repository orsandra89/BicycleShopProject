from django.contrib import admin
from .models import Brands, Customers, Categories, Stocks, Products, Staffs, Stores, Order_Items, Orders

admin.site.register(Brands)
admin.site.register(Customers)
admin.site.register(Categories)
admin.site.register(Stocks)
admin.site.register(Products)
admin.site.register(Staffs)
admin.site.register(Stores)
admin.site.register(Order_Items)
admin.site.register(Orders)