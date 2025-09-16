from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm
import os

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()

    # Fetch keys from environment variables
    stripe_public_key = os.getenv('STRIPE_PUBLIC_KEY')
    client_secret = os.getenv('STRIPE_CLIENT_SECRET')  # Or whatever this refers to

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)
