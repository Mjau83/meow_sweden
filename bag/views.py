from django.shortcuts import (render, redirect, reverse, HttpResponse,
                              get_object_or_404)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ Returns a view of the content of the bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add selected quantity of a product to shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'catear_color' in request.POST:
        color = request.POST['catear_color']
    if 'quipu_color_choise ' in request.POST:
        color = request.POST['quipu_color_choise']
    
    bag = request.session.get('bag', {})

    if color:
        if item_id in list(bag.keys()):
            if color in bag[item_id]['items_by_color'].keys():
                bag[item_id]['items_by_color'][color] += quantity
                messages.success(request, f'Updated {color.upper()} {product.name} quantity to {bag[item_id] ["items_by_color"][color]}')
            else:
                bag[item_id]['items_by_color'][color] = quantity
                messages.success(request, f'Added {color.upper()} {product.name} to your Shopping Bag')
        else:
            bag[item_id] = {'items_by_color': {color: quantity}}
            messages.success(request, f'Added {color.upper()} {product.name} to your Shopping Bag')
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Quantity of {product.name} is updated to {bag[item_id]}!')
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} was successfully added to your Shopping Bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag_items(request, item_id):
    """ Adjust quantity of products in the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))

    color = None
    if 'catear_color' in request.POST:
        color = request.POST['catear_color']
    bag = request.session.get('bag', {})

    if color:
        if quantity > 0:
            bag[item_id]['items_by_color'][color] = quantity
            messages.success(request, f'Updated {color.upper()} {product.name} quantity to {bag[item_id]["items_by_color"][color]}')
        else:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
            messages.success(request, f'Removed {color.upper()} {product.name} from your Shopping Bag')
    else:
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your Shopping Bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_bag_items(request, item_id):
    """ Remove selected product from shopping bag """

    try:
        product = get_object_or_404(Product, pk=item_id)
        color = None
        if 'catear_color' in request.POST:
            color = request.POST['catear_color']
        bag = request.session.get('bag', {})

        if color:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
            messages.success(request, f'Removed {color.upper()} {product.name} from your Shopping Bag')
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your Shopping Bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'An Error occured removing item: {e}')
        return HttpResponse(status=500)
