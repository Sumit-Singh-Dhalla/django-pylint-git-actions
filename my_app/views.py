"""
views file
"""
# Create your views here.
from django.http import HttpResponse


def complex_code():
    """ demo complex code to check for the linter to get failed """
    if True:
        if True:
            if True:
                if True:
                    if True:
                        if True:
                            return True


def hello(request):
    """
    simple hello world function based view
    """
    complex_code()
    return HttpResponse("Hello world!")
