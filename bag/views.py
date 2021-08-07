from django.shortcuts import render, redirect


def view_bag(request):
    """ Returns a view of the content of the bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add selected quantity of a product to shopping bag """

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

    request.session['bag'] = bag
    return redirect(redirect_url)
