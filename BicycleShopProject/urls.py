"""
URL configuration for BicycleShopProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BicycleShopProject.view import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='login'),
    path('bicycles/', views.get_bicycle_list, name='bicycle_list'),
    path('bicycles/<int:bicycle_id>/', views.get_bicycle_by_id, name='bicycle_detail'),
    path('customer/<int:customer_id>/orders', views.get_order_list_for_customer, name='order_list'),
    path('customer/<int:customer_id>/orders/<int:order_id>/', views.customer_order_ids, name='user_order_ids'),
    path('customer/<int:customer_id>/create_order/', views.create_order, name='create_order'),
    path('orders/<int:order_id>/add-item/<int:item_id>', views.add_item_to_order, name='add_item_to_order'),
    path('orders/<int:order_id>/delete-item/<int:item_id>', views.delete_item_from_order, name='delete_item_from_order'),
    path('orders/<int:order_id>/delete-all-items/', views.delete_all_items_from_order, name='delete_all_items_from_order'),
]
