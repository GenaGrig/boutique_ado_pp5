from django.shortcuts import render


def handler404(request, exception):
    """ A view to return a 404 error page """
    return render(request, 'errors/404.html', status=404)
