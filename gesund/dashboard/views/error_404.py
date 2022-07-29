from django.shortcuts import render


def error_404(request, exception):
    data = {}
    return render(request, 'errors/404.html', status=404)
