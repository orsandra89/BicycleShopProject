import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from BicycleShopProject.models.models import Product, Order, Customer, OrderItem, Stock
from django.http import JsonResponse
from django.views.decorators.http import require_GET, require_POST
import logging

from datetime import datetime

# def bicycle_list(request):
#     bicycles = Product.objects.all()
#     return render(request, {'bicycles': bicycles})
#
# def bicycle_detail(request, id):
#     bicycle = get_object_or_404(Product, pk=id)
#     return render(request, {'bicycle': bicycle})

logger = logging.getLogger(__name__)
@api_view(['GET'])
@permission_classes([AllowAny])
def get_bicycle_list(request):
    bicycles = Product.objects.all()
    bicycle_list = []
    for bicycle in bicycles:
        bicycle_list.append({
            'id': bicycle.product_id,
            'product_name': bicycle.product_name,
            'brand': bicycle.brand_id.brand_name,
            'category': bicycle.category_id.category_name,
            'price': bicycle.list_price
        })
    return JsonResponse({'bicycles': bicycle_list})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_bicycle_by_id(request, bicycle_id):
    try:
        bicycle = Product.objects.get(product_id=bicycle_id)
        bicycle_data = {
            'id': bicycle.product_id,
            'product_name': bicycle.product_name,
            'brand': bicycle.brand_id.brand_name,
            'category': bicycle.category_id.category_name,
            'price': bicycle.list_price
        }
        return JsonResponse(bicycle_data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Bicycle not found'}, status=404)

@api_view(['GET'])
def get_order_list_for_customer(request, customer_id):
    try:
        orders = Order.objects.filter(customer_id=customer_id)
        order_list = []
        for order in orders:
            order_list.append({
                'id': order.order_id,
                'customer_name': order.customer_id.first_name,
                'customer_last_name': order.customer_id.last_name,
                'order_status': order.order_status,
                'order_date': order.order_date,
                'store_name': order.store_id.store_name,
                'seller_name': order.staff_id.first_name,
                'seller_last_name': order.staff_id.last_name
            })
        return JsonResponse({'customer_orders': order_list})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'User has no orders'}, status=404)

# @require_GET
@api_view(['GET'])
def customer_order_ids(request, customer_id, order_id):
    try:
        order = Order.objects.get(customer_id=customer_id, order_id=order_id)
        items = list(OrderItem.objects.filter(order_id=order_id).values())
        order_data = {
            'id': order.order_id,
            'customer_name': order.customer_id.first_name,
            'customer_last_name': order.customer_id.last_name,
            'order_status': order.order_status,
            'order_date': order.order_date,
            'items': items,
            'store': order.store_id,
            'seller': order.staff_id
        }
        return JsonResponse(order_data)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found for the user'}, status=404)



@api_view(['POST'])
def create_order(request, customer_id):
    try:
        customer = get_object_or_404(Customer, customer_id=customer_id)
        data = json.loads(request.body)
        # Retrieve fields from the parsed data
        order_id = data.get('order_id')
        state = Order.DRAFT
        n = datetime.now().date()

        # Check if user_id and product_id are provided
        if not order_id:
            return JsonResponse({'error': 'User ID, Order ID are required'}, status=400)

        # Create the order
        order = Order.objects.create(
            customer_id=customer,
            order_id=order_id,
            order_status=state,
            order_date= n
        )

        return JsonResponse({'order_id': order.order_id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@api_view(['POST'])
def add_item_to_order(request, order_id, item_id):
    try:
        order = get_object_or_404(Order, order_id=order_id)
        data = json.loads(request.body)

        # Extract fields from the request data
        product_id = data.get('product_id')
        quantity = data.get('quantity')

        # Validate required fields
        if not all([product_id, quantity]):
            return JsonResponse({'error': 'Product ID and Quantity are required'}, status=400)

        # Retrieve the product
        product = get_object_or_404(Product, pk=product_id)

        try:
            stock = Stock.objects.get(product_id=product)
            if stock.quantity < quantity:
                return JsonResponse({'error': 'Insufficient stock quantity'}, status=400)
        except Stock.DoesNotExist:
            return JsonResponse({'error': 'Product is out of stock'}, status=400)

        # Create the order item

        try:
            order_item = OrderItem.objects.get(order_id=order, product_id=product)
            if stock.quantity < quantity + order_item.quantity:
                return JsonResponse({'error': 'Insufficient stock quantity'}, status=400)
            order_item.quantity += quantity
            order_item.save(update_fields=['quantity'])
            return JsonResponse({'order_item_id': order_item.order_item_id}, status=201)

        except OrderItem.DoesNotExist:
            order_item = OrderItem.objects.create(
                order_id=order,
                product_id=product,
                quantity=quantity,
                list_price=product.list_price,
                discount=0
            )
            return JsonResponse({'order_item_id': order_item.order_item_id}, status=201)


        return JsonResponse({'order_item_id': order_item.order_item_id}, status=201)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product does not exist'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

# @require_POST
# def register(request):
#     form = UserCreationForm(request.POST)
#     if form.is_valid():
#         form.save(commit=False)
#         form.cleaned_data['username'] = form.cleaned_data['email']  # Use email as username
#         form.save()
#         username = form.cleaned_data.get('email')
#         raw_password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=raw_password)
#         login(request, user)
#         return redirect('home')  # Redirect to the desired page after registration
#     else:
#         return JsonResponse({'error': 'Invalid form data'}, status=400)
#
# @require_POST
# def user_login(request):
#     form = AuthenticationForm(request, request.POST)
#     if form.is_valid():
#         user = form.get_user()
#         login(request, user)
#         return redirect('home')  # Redirect to the desired page after login
#     else:
#         return JsonResponse({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
def delete_item_from_order(request, order_id, item_id):
    try:
        get_object_or_404(Order, order_id=order_id)
        order_item = get_object_or_404(OrderItem, order_item_id=item_id)
        order_item.delete()

        return JsonResponse({'message': 'Order item deleted successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@api_view(['POST'])
def delete_all_items_from_order(request, order_id):
    try:
        for order in list(OrderItem.objects.filter(order_id= order_id)):
            order.delete()

        return JsonResponse({'message': 'All items from the order have been deleted successfully'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

@api_view(['POST'])
def change_order_status(request, order_id):
    try:
        order = get_object_or_404(Order, pk=order_id)
        order_items = OrderItem.objects.filter(order_id=order)

        for order_item in order_items:
            product = order_item.product_id
            stock = Stock.objects.get(product_id=product)

            if stock.quantity < order_item.quantity:
                return JsonResponse(
                    {'error': 'Insufficient stock quantity for product {}'.format(product.product_name)}, status=400)

            order.order_status = Order.PENDING
            order.save()

            stock.quantity = stock.quantity - order_item.quantity
            stock.save()

        return JsonResponse({'message': 'Order status updated successfully', 'new_status': Order.PENDING}, status=200)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order does not exist'}, status=404)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product does not exist'}, status=404)
    except Stock.DoesNotExist:
        return JsonResponse({'error': 'Stock for product does not exist'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)