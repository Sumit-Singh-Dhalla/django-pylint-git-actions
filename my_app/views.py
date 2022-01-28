"""
views file
"""
# Create your views here.
from django.http import HttpResponse


def hello(request):
    """
    simple hello world function based view
    """
    return HttpResponse("Hello world!")
