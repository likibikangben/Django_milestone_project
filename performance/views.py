from django.shortcuts import render

# Create your views here.

def line_up(request):
    """ A view to show the line up """

    return render(request, 'performance/line_up.html')

def location(request):
    """ A view to show a google map location of the event """

    return render(request, 'location.html')
