from django.shortcuts import render


def index(request):
    """ Returns a view of the content of the bag """

    return render(request, 'bag/bag.html')
