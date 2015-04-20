from django.core.management.base import BaseCommand, CommandError
from graph.models import Website

class Command(BaseCommand):
	help = 'Init database using seeds'

	def handle(self, *args, **options):
		w = Website(name="New York Times", url="http://nytimes.com", rss_url="http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
		w.save()
		w.download_rss_articles()
