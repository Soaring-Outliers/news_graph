from django.shortcuts import render
from django.http import HttpResponseRedirect
from graph.forms import WebsiteForm

from django.views.generic.list import ListView
from django.utils import timezone

from graph.models import Website, Article, Concept, ArticleConcept

def graph(request):
    from .helpers import to_dict, to_json
    concept_type = {
        "id": 0, 
        "color": "#FFAAFF", 
        "node_ids": [-id for id in Concept.objects.values_list('id', flat=True)],
    }
    articleconcept_type = {
        "id": 1, 
        "color": "#FFAAFF", 
        "link_ids": list(ArticleConcept.objects.values_list('id', flat=True)),
    }
    data_for_graph = {
        "nodes-by-id": to_json(Article.objects.all(), Concept.objects.all()),
        "links-by-id": to_json(ArticleConcept.objects.all()),
        "type-nodes-by-id": to_json(Website.objects.all(), [concept_type]),
        "type-links-by-id": to_json([articleconcept_type]),
        "modifiable-node-ids": "[]",
    }
    websites = Website.objects.all()
    articles = Article.objects.all()
    concepts = Concept.objects.all()
    articleconcepts = ArticleConcept.objects.all()
            
    return render(request, 'graph/graph.html', {
        'data_for_graph': data_for_graph,
        'websites': websites,
        'articles': articles,
        'concepts': concepts,
        'articleconcepts': articleconcepts,
        'concept_type': concept_type,
        'articleconcept_type': articleconcept_type,
    })
    
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