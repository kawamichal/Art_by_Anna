from django.contrib import admin

from orders.models import OrderItem, Order


class OrderItemInline(admin.TabularInline):  # order items will be displayed on the same page as orders
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created']
