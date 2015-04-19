from django.test import TestCase

# Create your tests here.
from graph.models import Website, Article
import datetime


class WebsiteMethodTests(TestCase):

    def test_download_rss_articles_1(self):
        """
        download_rss_articles should return a list of articles saved in DB
        """
        website = Website(name="NYTimes", url="https://nytimes.com", rss_url="http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
        website.save()
        self.assertNotEqual(website.download_rss_articles(), [])
        #self.assertNotEqual(website.download_rss_articles(), []) # Normally way more quicker

    def test_download_rss_articles_2(self):
        """
        Same as above, for another website
        """
        """
        website = Website(name="20 minutes", url="https://20minutes.fr", rss_url="http://flux.20minutes.fr/c/32497/f/479493/index.rss")
        website.save()
        self.assertNotEqual(website.download_rss_articles(), [])
        """
        
    def test_fill_alchemy_1(self):
        """
        website = Website(name="NYTimes", url="https://nytimes.com", rss_url="http://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")
        website.save()
        article = Article(
            website=website, 
            title="Fake Article", 
            description="Fake description", 
            url="http://www.20minutes.fr/sport/1590259-20150419-direct-coupe-europe-leinster-efficace-melee-toulonnaise-fait-manger#xtor=RSS-145", 
            rss_url="fake_url",
            date= datetime.datetime.now(),
            content="Fake content")
        try:
            article.save()
        except Exception as e:
            print("KO: ",e)
        self.assertIsNotNone(article.entities_xml)
        """