from django.shortcuts import render
from django.http import HttpResponseRedirect
from graph.forms import WebsiteForm

from django.views.generic.list import ListView
from django.utils import timezone

from graph.models import Website

def graph(request):
    return render(request, 'graph/graph.html')
    
def website_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WebsiteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            
            # redirect to a new URL:
            return HttpResponseRedirect('/website')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = WebsiteForm()

    return render(request, 'graph/website_form.html', {'form': form})

class WebsiteListView(ListView):

    model = Website

    def get_context_data(self, **kwargs):
        context = super(WebsiteListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context