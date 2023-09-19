from django.shortcuts import render
from django.views import generic

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


class MainPageView(generic.TemplateView):
    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Boutique Ado'
        return context
