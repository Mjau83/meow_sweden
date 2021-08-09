from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ Returns a view of the content of the bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add selected quantity of a product to shopping bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    color = None
    if 'catear_color' in request.POST:
        color = request.POST['catear_color']
    bag = request.session.get('bag', {})

    if color:
        if item_id in list(bag.keys()):
            if color in bag[item_id]['items_by_color'].keys():
                bag[item_id]['items_by_color'][color] += quantity
            else:
                bag[item_id]['items_by_color'][color] = quantity
        else:
            bag[item_id] = {'items_by_color': {color: quantity}}
    else:
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'{product.name} was successfully added to your Shopping Bag!')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag_items(request, item_id):
    """ Adjust quantity of products in the shopping bag """

    quantity = int(request.POST.get('quantity'))

    color = None
    if 'catear_color' in request.POST:
        color = request.POST['catear_color']
    bag = request.session.get('bag', {})

    if color:
        if quantity > 0:
            bag[item_id]['items_by_color'][color] = quantity
        else:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
    else:
        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_bag_items(request, item_id):
    """ Remove selected product from shopping bag """

    try:
        color = None
        if 'catear_color' in request.POST:
            color = request.POST['catear_color']
        bag = request.session.get('bag', {})

        if color:
            del bag[item_id]['items_by_color'][color]
            if not bag[item_id]['items_by_color']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
