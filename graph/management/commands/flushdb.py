from django.core.management.base import BaseCommand, CommandError
from graph.models import Article, Concept, ArticleConcept

class Command(BaseCommand):
	help = 'Flush database but keeps website'

	def handle(self, *args, **options):
	    Article.objects.all().delete()
	    Concept.objects.all().delete()
	    ArticleConcept.objects.all().delete()
	    