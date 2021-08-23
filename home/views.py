from django.shortcuts import render


def index(request):
    """ Returns index page view """

    return render(request, 'home/index.html')

def about(request):
    """ Returns about page view """
    return render(request, 'home/about.html')
