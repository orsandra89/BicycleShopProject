from django.contrib import admin
from django.core.checks import messages
from django.shortcuts import redirect
from django.template.defaulttags import url

from .models import Brand, Categorie, Stock, Product, User, OrderItem, Order
from django.utils.html import format_html
from django.urls import reverse
from django.urls import path
from django.db import transaction

admin.site.register(Categorie)
admin.site.register(Stock)
admin.site.register(Product)
admin.site.register(User)
admin.site.register(OrderItem)


class BrandAdmin(admin.ModelAdmin):
    list_display = ["brand_id", "brand_name"]
    ordering = ["brand_id"]
    readonly_fields = ["brand_id"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["order_id", "order_status", "order_date", "required_date", "shipped_date", 'order_actions']
    ordering = ["order_id"]
    actions = ["reject_order"]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:order_id>/reject/', self.admin_site.admin_view(self.reject_order), name='order-reject'),
            path('<int:order_id>/process/', self.admin_site.admin_view(self.process_order), name='order-process'),
            path('<int:order_id>/complete/', self.admin_site.admin_view(self.complete_order), name='order-complete')
        ]
        return custom_urls + urls

    def order_actions(self, obj):
        if obj.order_status == Order.PENDING:
            return format_html(
                '<a class="button" href="{}">Process</a>',
                reverse('admin:order-process', args=[obj.order_id]),
            )
        elif obj.order_status == Order.PROCESSING:
            return format_html(
                '<a class="button" href="{}">Reject</a>&nbsp;'
                '<a class="button" href="{}">Complete</a>&nbsp;',
                reverse('admin:order-reject', args=[obj.order_id]),
                reverse('admin:order-complete', args=[obj.order_id]),
            )
        return ""

    order_actions.short_description = 'Order Actions'
    order_actions.allow_tags = True

    @admin.action(description="Mark order as rejected")
    def reject_order(self, request, order_id, *args, **kwargs):
        order = self.get_object(request, order_id)
        if order:
            with transaction.atomic():
                order.order_status = Order.REJECTED
                order.save()

                order_items = OrderItem.objects.filter(order=order)


                for order_item in order_items:
                    product = order_item.product
                    stock = Stock.objects.get(product=product)

                    stock.quantity = stock.quantity + order_item.quantity
                    stock.save()

            self.message_user(request, "Order rejected.")
        else:
            self.message_user(request, "Order not found.", level=messages.ERROR)

        return redirect('../..')

    @admin.action(description="Mark order as processing")
    def process_order(self, request, order_id, *args, **kwargs):
        order = self.get_object(request, order_id)
        if order:
            order.order_status = Order.PROCESSING
            order.save()

            self.message_user(request, "Order Processed.")
        else:
            self.message_user(request, "Order not found.", level=messages.ERROR)

        return redirect('../..')

    @admin.action(description="Mark order as completed")
    def complete_order(self, request, order_id, *args, **kwargs):
        order = self.get_object(request, order_id)
        if order:
            order.order_status = Order.COMPLETED
            order.save()

            self.message_user(request, "Order Completed.")
        else:
            self.message_user(request, "Order not found.", level=messages.ERROR)

        return redirect('../..')


admin.site.register(Brand, BrandAdmin)
admin.site.register(Order, OrderAdmin)
