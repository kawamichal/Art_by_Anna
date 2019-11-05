from django.db import models

# a model that will let the owner generate a PDF invoice
from shop.models import Product


class Order(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # contact details
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    # status
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)  # - for reverse order

    def __str__(self):
        return 'Order {}'.format(self.id)  # a unique representation of each invoice

    def get_total_cost(self):  # total cost of all items in cart
        return sum(item.get_cost() for item in self.items.all())  # items defined below as OrderItem


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    braintree_id = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
