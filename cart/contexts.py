from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Ensures that the cart context are available when rendering every page
    """

    cart = request.session.get('cart', {})
    # Set some empty variables 
    cart_items = []
    total = 0
    product_count = 0
    # for everything in the cart.items()
    # where is cart.items defined it is made up in this
    for id, quantity in cart.items():
        product = get_object_or_404(Product, pk=id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity':quantity, 'product':product})

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count }