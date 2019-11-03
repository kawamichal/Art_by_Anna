from decimal import Decimal

from django.conf import settings

from shop.models import Product


class Cart(object):
    def __init__(self, request):
        self.session = request.session  # starting a session
        cart = self.session.get(settings.CART_SESSION_ID)  # in case there is cart
        if not cart:  # in case there is no cart
            cart = self.session[settings.CART_SESSION_ID] = {}  # starting an empty cart (session is a dict!)
        self.cart = cart  # create cart in either case

    def add(self, product, quantity=1, update_quantity=False):  # adding products to a cart
        product_id = product.id  # assigning id of the added product to a variable
        if product_id not in self.cart:  # if the product is not in the cart
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:  # if true - update the quantity
            self.cart[product_id]['quantity'] = quantity
        else:  # if false - add to the existing quantity,
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True  # inform Django that the session is modified and has to be saved

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):  # iteration through ids to get the product attributes
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['item'] * item['quantity']
            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
