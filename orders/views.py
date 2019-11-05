from django.shortcuts import render, redirect
from django.urls import reverse

from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem

def order_create(request):
    cart = Cart(request) # fetch the existing cart
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save() # create an instance of order
            for item in cart: # adding the items from cart into an order
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear() # clearing the cart after posting an order
            request.session['order_id'] = order.id #adding id of an order instance to the session
            return redirect(reverse('payment:process'))
    else: # if request.method == 'GET':
        form = OrderCreateForm()
    return render(request,
                  'orders/create.html',
                  {'cart': cart, 'form': form})