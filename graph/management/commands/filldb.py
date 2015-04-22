from django.core.management.base import BaseCommand, CommandError
from graph.models import Website

class Command(BaseCommand):
    help = 'Fill database by retrieving articles and concepts'

    def handle(self, *args, **options):
        for website in Website.objects.all():
            print(website.name)
            website.download_rss_articles()