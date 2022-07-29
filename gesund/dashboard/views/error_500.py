from django.shortcuts import render


def error_500(request, *args, **argv):
    """ get if there's an error 500. """
    data = {}
    return render(request, 'errors/500.html', status=500)
