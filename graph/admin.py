from django.contrib import admin

# Register your models here.
from .models import Website, Article, Concept, ArticleConcept

admin.site.register(Website)
admin.site.register(Article)
admin.site.register(Concept)
admin.site.register(ArticleConcept)