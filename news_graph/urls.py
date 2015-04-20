from django.conf.urls import patterns, include, url
from django.contrib import admin
from graph.views import WebsiteListView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'news_graph.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'graph.views.graph', name='graph'),
    
    url(r'^website-form/', 'graph.views.website_form', name='website-form'),
    url(r'^website', WebsiteListView.as_view(), name='website-list'),
)
