import json

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.hashers import make_password
from django.db import transaction

from BicycleShopProject.models.models import Product, Order, OrderItem, Stock, User
from django.http import JsonResponse
import logging

from datetime import datetime


logger = logging.getLogger(__name__)

# TODO transaction


@csrf_exempt
@api_view(['GET'])
@permission_classes([AllowAny])
def get_bicycle_list(request):
    bicycles = Product.objects.all()
    bicycle_list = []
    for bicycle in bicycles:
        stock = Stock.objects.filter(product=bicycle).first()
        default_quantity = 0
        quantity = stock.quantity if stock else default_quantity
        bicycle_list.append({
            'id': bicycle.product_id,
            'product_name': bicycle.product_name,
            'brand': bicycle.brand.brand_name,
            'category': bicycle.category.category_name,
            'price': bicycle.list_price,
            'quantity': quantity
        })
    return JsonResponse({'bicycles': bicycle_list})


@api_view(['GET'])
@permission_classes([AllowAny])
@csrf_exempt
def get_bicycle_by_id(request, bicycle_id):
    try:
        bicycle = Product.objects.get(product_id=bicycle_id)
        stock = Stock.objects.filter(product=bicycle).first()
        default_quantity = 0
        quantity = stock.quantity if stock else default_quantity
        bicycle_data = {
            'id': bicycle.product_id,
            'product_name': bicycle.product_name,
            'brand': bicycle.brand.brand_name,
            'category': bicycle.category.category_name,
            'price': bicycle.list_price,
            'quantity': quantity
        }
        return JsonResponse(bicycle_data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Bicycle not found'}, status=404)


@api_view(['GET'])
@csrf_exempt
def get_order_list_for_customer(request, user_id):
    try:
        user = User.objects.get(user_id=user_id)
        orders = Order.objects.filter(user=user)
        order_list = []
        for order in orders:
            order_list.append({
                'id': order.order_id,
                'user_name': order.user.first_name,
                'usr_last_name': order.user.last_name,
                'order_status': order.order_status,
                'order_date': order.order_date
            })
        return JsonResponse({'customer_orders': order_list})
    except Order.DoesNotExist:
        return JsonResponse({'error': 'User has no orders'}, status=404)


@api_view(['GET'])
@csrf_exempt
def customer_order_ids(request, user_id, order_id):
    try:
        user = User.objects.get(user_id=user_id)
        order = Order.objects.get(user=user, order_id=order_id)
        items = list(OrderItem.objects.filter(order=order).values())
        order_data = {
            'id': order.order_id,
            'customer_name': order.user.first_name,
            'customer_last_name': order.user.last_name,
            'order_status': order.order_status,
            'order_date': order.order_date,
            'items': items,
            'seller': order.staff_id
        }
        return JsonResponse(order_data)
    except Order.DoesNotExist:
        return JsonResponse({'error': 'Order not found for the user'}, status=404)


@api_view(['POST'])
@csrf_exempt
def create_order(request, user_id):
    try:
        user = get_object_or_404(User, user_id=user_id)

        state = Order.DRAFT
        n = datetime.now().date()

        order = Order.objects.filter(user=user, order_status=state).first()

        if order is None:
            order = Order.objects.create(
                user=user,
                order_status=state,
                order_date=n
            )

        return JsonResponse({'order_id': order.order_id}, status=201)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
@csrf_exempt
def add_item_to_order(request, order_id):
    try:
        order = get_object_or_404(Order, order_id=order_id)
        if order.order_status is Order.DRAFT:
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
                stock = Stock.objects.get(product=product)
                if stock.quantity < quantity:
                    return JsonResponse({'error': 'Insufficient stock quantity'}, status=400)
            except Stock.DoesNotExist:
                return JsonResponse({'error': 'Product is out of stock'}, status=400)

            # Create the order item

            try:
                order_item = OrderItem.objects.get(
                    order=order, product=product)
                if stock.quantity < quantity + order_item.quantity:
                    return JsonResponse({'error': 'Insufficient stock quantity'}, status=400)
                order_item.quantity += quantity
                order_item.save(update_fields=['quantity'])
                return JsonResponse({'order_item_id': order_item.order_item_id}, status=201)

            except OrderItem.DoesNotExist:
                order_item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    list_price=product.list_price,
                    discount=0
                )
                return JsonResponse({'order_item_id': order_item.order_item_id}, status=201)

            return JsonResponse({'order_item_id': order_item.order_item_id}, status=201)
        else:
            return JsonResponse({'error': 'Order already send to realization'}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product does not exist'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
@csrf_exempt
def delete_item_from_order(request, order_id, item_id):
    try:
        order = get_object_or_404(Order, order_id=order_id)
        order_item = get_object_or_404(OrderItem, order_item_id=item_id)
        if order.order_status is Order.DRAFT:
            order_item.delete()

            return JsonResponse({'message': 'Order item deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Order already send to realization'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
@csrf_exempt
def delete_all_items_from_order(request, order_id):
    try:
        order = get_object_or_404(Order, order_id=order_id)
        if order.order_status is Order.DRAFT:
            with transaction.atomic():
                for order in list(OrderItem.objects.filter(order=order)):
                    order.delete()

            return JsonResponse({'message': 'All items from the order have been deleted successfully'}, status=200)
        else:
            return JsonResponse({'error': 'Order already send to realization'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


@api_view(['POST'])
@csrf_exempt
def change_order_status(request, order_id):
    try:
        order = get_object_or_404(Order, pk=order_id)
        order_items = OrderItem.objects.filter(order=order)

        with transaction.atomic():
            for order_item in order_items:
                product = order_item.product
                stock = Stock.objects.get(product=product)

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


@api_view(['POST'])
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user = User.objects.create(
            username=data['email'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            email=data['email'],
            password=make_password(data['password'])
        )
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return JsonResponse({'message': 'User and Customer created successfully'}, status=201)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)


@api_view(['POST'])
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({
                'message': 'User logged in successfully',
                'is_superuser': user.is_superuser,
                'username': user.username
            }, status=200)
        else:
            return JsonResponse({'error': 'Invalid login credentials'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
