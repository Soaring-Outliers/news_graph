from django.test import TestCase

# Create your tests here.
from graph.models import Website, Article
import datetime
from django.conf import settings
URL = "http://news-graph-pidupuis-2.c9.io"

class WebsiteMethodTests(TestCase):

    def test_download_rss_articles_1(self):
        """
        download_rss_articles should return a list of articles saved in DB
        """
        if False: #Long test, activate on demand
            url = URL+settings.STATIC_URL+"graph/xml/nytimes.rss.xml"
            website = Website(name="NYTimes", url="https://nytimes.com", rss_url=url)
            website.save()
            articles = website.download_rss_articles()
            self.assertNotEqual(articles, [])
            self.assertEqual(len(articles), 20)
            a1 = articles[0]
            self.assertEqual(a1.title, "Praise and Skepticism as One Executive Sets Minimum Wage to $70,000 a Year")
            self.assertEqual(a1.rss_url, "http://rss.nytimes.com/c/34625/f/640350/s/458934ea/sc/7/l/0L0Snytimes0N0C20A150C0A40C20A0Cbusiness0Cpraise0Eand0Eskepticism0Eas0Eone0Eexecutive0Esets0Eminimum0Ewage0Eto0E70A0A0A0A0Ea0Eyear0Bhtml0Dpartner0Frss0Gemc0Frss/story01.htm")
            self.assertEqual(a1.url, "http://www.nytimes.com/2015/04/20/business/praise-and-skepticism-as-one-executive-sets-minimum-wage-to-70000-a-year.html?partner=rss&emc=rss&_r=0")
            
            a2 = articles[-1]
            self.assertEqual(a2.title, "Sale of U.S. Arms Fuels the Wars of Arab States")
            self.assertEqual(a2.rss_url, "http://rss.nytimes.com/c/34625/f/640350/s/458758c2/sc/11/l/0L0Snytimes0N0C20A150C0A40C190Cworld0Cmiddleeast0Csale0Eof0Eus0Earms0Efuels0Ethe0Ewars0Eof0Earab0Estates0Bhtml0Dpartner0Frss0Gemc0Frss/story01.htm")
            self.assertEqual(a2.url, "http://www.nytimes.com/2015/04/19/world/middleeast/sale-of-us-arms-fuels-the-wars-of-arab-states.html?partner=rss&emc=rss&_r=0")
            
            articles2 = website.download_rss_articles() # Normally way more quick
            self.assertNotEqual(articles2, [])
            self.assertEqual(articles2[0], a1)
            self.assertEqual(articles2[-1], a2)
        
    def test_download_rss_articles_2(self):
        """
        Same as above, for another website
        """
        if False: #Long test, activate on demand
            url = URL+settings.STATIC_URL+"graph/xml/20minutes.rss.xml"
            website = Website(name="20 minutes", url="https://20minutes.fr", rss_url=url)
            website.save()
            articles = website.download_rss_articles()
            self.assertNotEqual(articles, [])
            self.assertEqual(len(articles), 20)
            a1 = articles[10]
            self.assertEqual(a1.title.encode('utf-8'), b"Coupe d'Europe: La qualification difficile de Toulon en finale \xc3\xa0 revivre en direct comme-\xc3\xa0-la-maison (25-20)")
            self.assertEqual(a1.rss_url, 'http://flux.20minutes.fr/c/32497/f/479493/s/4586ffcf/sc/13/l/0L0S20Aminutes0Bfr0Carticle0C1590A2590Crss0Emediafed0E1590A2590Txtor0FRSS0E145/story01.htm')
            self.assertEqual(a1.url, 'http://www.20minutes.fr/sport/1590259-20150419-coupe-europe-qualification-difficile-toulon-finale-revivre-direct-comme-maison-25-20')
            self.assertEqual(a1.date, datetime.datetime(2015, 4, 19, 16, 46, 21))
        
    def test_fill_alchemy_1(self):
        if True: #Long test, activate on demand
            url = URL+settings.STATIC_URL+"graph/xml/nytimes.rss.xml"
            website = Website(name="NYTimes", url="https://nytimes.com", rss_url=url)
            website.save()
            article = Article(
                website=website, 
                title="Fake Article", 
                description="Fake description", 
                url="http://www.nytimes.com/2015/04/20/world/middleeast/isis-video-purports-to-show-killing-of-ethiopian-christians.html?partner=rss&emc=rss", 
                rss_url="fake_url",
                date= datetime.datetime.now(),
                content="Fake content")
            try:
                article.save()
            except Exception as e:
                self.assertFalse("KO: "+str(e))
            self.assertIsNotNone(article.concepts_xml)
            
            article_concepts = article.articleconcept_set.all()
            self.assertEqual(len(article_concepts), 8)
            self.assertEqual(article_concepts.first().relevance, 0.95995)
            self.assertEqual(article_concepts.last().relevance, 0.57948)
            
            concepts = article.concepts.all()
            self.assertEqual(len(concepts), 8)
            self.assertEqual(concepts.first().name, "Egypt")
            self.assertEqual(concepts.last().name, "Libya")
            