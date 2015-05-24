from django.shortcuts import render
from django.http import HttpResponseRedirect
from graph.forms import WebsiteForm

from django.views.generic.list import ListView
from django.utils import timezone

from graph.models import Website, Article, Concept, ArticleConcept
        
# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

import time
def tim(t, text):
    logger.error(text)
    logger.error(time.time()-t)
    #time.sleep(3)
    return time.time()
    

def graph(request):
    from .helpers import to_dict, to_json
    t=time.time()
    concept_type = {
        "id": 0, 
        "color": "#FF6699", 
        "node_ids": [-id for id in Concept.objects.filter(articles_count__gt=1).values_list('id', flat=True)],
    }
    t=tim(t, '#################### Concept_type ok! #####################')
    articleconcept_type = {
        "id": 1, 
        "color": "#FFAAAA", 
        "link_ids": list(ArticleConcept.objects.prefetch_related('concept').filter(concept__articles_count__gt=1).values_list('id', flat=True)),
    }
    t=tim(t, '#################### ArticleConcept_type ok! #####################')
    
    nodes_by_id = to_json(Article.objects.all(), Concept.objects.all())
    t=tim(t, '#################### nodes_by_id ok! #####################')
    links_by_id = to_json(ArticleConcept.objects.all())
    t=tim(t, '#################### links_by_id ok! #####################')
    type_nodes_by_id = to_json(Website.objects.all(), [concept_type])
    t=tim(t, '#################### type_nodes_by_id ok! #####################')
    type_links_by_id = to_json([articleconcept_type])
    t=tim(t, '#################### type_links_by_id ok! #####################')
    data_for_graph = {
        "nodes-by-id": nodes_by_id,
        "links-by-id": links_by_id,
        "type-nodes-by-id": type_nodes_by_id,
        "type-links-by-id": type_links_by_id,
        "modifiable-node-ids": "[]",
    }
    t=tim(t, '#################### DataForGraph ok! #####################')
    websites = Website.objects.all()
    t=tim(t, '#################### Websites ok! #####################')
    articles = Article.objects.prefetch_related('articleconcept_set__concept__articleconcept_set__article').all()
    t=tim(t, '#################### Articles ok! #####################')
    concepts = Concept.objects.prefetch_related('articleconcept_set__article').all()
    t=tim(t, '#################### Concepts ok! #####################')
    #articleconcepts = ArticleConcept.objects.all()
            
    return render(request, 'graph/graph.html', {
        'data_for_graph': data_for_graph,
        'websites': websites,
        'articles': articles,
        'concepts': concepts,
        #'articleconcepts': articleconcepts,
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