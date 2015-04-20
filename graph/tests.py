from django.test import TestCase

# Create your tests here.
from graph.models import Website, Article, Concept, ArticleConcept
import datetime
from django.conf import settings
from django.core import serializers
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
        if False: #Long test, activate on demand
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
                article.fill_alchemy()
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
            
    def test_json_by_id_1(self):
        if False:
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
                article.fill_alchemy()
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
            
            from django.core.serializers.python import Serializer
            import json
            from django.core.serializers.json import DjangoJSONEncoder
            class JSONByIdSerializer(Serializer):
                def get_dump_object(self, obj):
                    data = self._current
                    if not self.selected_fields or 'id' in self.selected_fields:
                        data['id'] = obj.id
                    return data2
            
                def end_object(self, obj):
                    if not self.first:
                        self.stream.write(', ')
                    self.stream.write(str(obj.id))
                    self.stream.write(": ")
                    #json.dump(self.get_dump_object(obj), self.stream,
                    #          cls=DjangoJSONEncoder)
                    json.dump(obj.json_attributes(), self.stream)
                    self._current = None
            
                def start_serialization(self):
                    self.stream.write("{")
            
                def end_serialization(self):
                    self.stream.write("}")
            
                def getvalue(self):
                    return super(Serializer, self).getvalue()
                    
            serializer = JSONByIdSerializer()
            self.assertEqual(serializer.serialize(Website.objects.all()), 
                '{1: {"node_ids": [1]}}')
            import ast
            self.assertEqual(ast.literal_eval(serializer.serialize(Website.objects.all())), 
                {1: {"node_ids": [1]}})
            
            self.assertEqual(ast.literal_eval(serializer.serialize(Article.objects.all()).replace('false', 'False').replace('true', 'True')), 
                {1: {"name": "Fake Article", "id": 1, "display_name": False, "importance": 1, "depth": 0}})
            
            self.assertEqual(ast.literal_eval(serializer.serialize(Concept.objects.all()).replace('false', 'False').replace('true', 'True')), 
                {1: {"name": "Egypt", "id": 1, "display_name": True, "importance": 1, "depth": 0}, 2: {"name": "Islam", "id": 2, "display_name": True, "importance": 1, "depth": 0}, 3: {"name": "Arabic language", "id": 3, "display_name": True, "importance": 1, "depth": 0}, 4: {"name": "Syria", "id": 4, "display_name": True, "importance": 1, "depth": 0}, 5: {"name": "Israel", "id": 5, "display_name": True, "importance": 1, "depth": 0}, 6: {"name": "Caliphate", "id": 6, "display_name": True, "importance": 1, "depth": 0}, 7: {"name": "Ottoman Empire", "id": 7, "display_name": True, "importance": 1, "depth": 0}, 8: {"name": "Libya", "id": 8, "display_name": True, "importance": 1, "depth": 0}})
            
            self.assertEqual(ast.literal_eval(serializer.serialize(ArticleConcept.objects.all()).replace('false', 'False').replace('true', 'True')), 
                {1: {"targetID": 1, "name": "Fake Article <-0.95995-> Egypt", "id": 1, "sourceID": 1}, 2: {"targetID": 2, "name": "Fake Article <-0.906098-> Islam", "id": 2, "sourceID": 1}, 3: {"targetID": 3, "name": "Fake Article <-0.853767-> Arabic language", "id": 3, "sourceID": 1}, 4: {"targetID": 4, "name": "Fake Article <-0.688198-> Syria", "id": 4, "sourceID": 1}, 5: {"targetID": 5, "name": "Fake Article <-0.624983-> Israel", "id": 5, "sourceID": 1}, 6: {"targetID": 6, "name": "Fake Article <-0.611671-> Caliphate", "id": 6, "sourceID": 1}, 7: {"targetID": 7, "name": "Fake Article <-0.611542-> Ottoman Empire", "id": 7, "sourceID": 1}, 8: {"targetID": 8, "name": "Fake Article <-0.57948-> Libya", "id": 8, "sourceID": 1}})
            
            
            print(serializer.serialize(Website.objects.all()))
            #print(serializers.serialize("json", Article.objects.all(), fields=('title', 'fake_method')))
            #print(article.json_attributes())
        
    def test_json_by_id_2(self):
        if True:
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
                article.fill_alchemy()
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
            
            from .helpers import to_dict, to_json
                
            concept_type = {
                "id": 0, 
                "color": "#FFAAFF", 
                "node_ids": [-id for id in Concept.objects.values_list('id', flat=True)],
            }
            # Type_nodes_by_id
            self.assertEqual(to_dict(Website.objects.all(), [concept_type]), 
                {0: {'id': 0, 'color': '#FFAAFF', 'node_ids': [-1, -2, -3, -4, -5, -6, -7, -8]}, 1: {'id': 1, 'node_ids': [1]}})
            # Nodes_by_id
            self.assertEqual(to_dict(Article.objects.all(), Concept.objects.all()), 
                {1: {'importance': 1, 'display_name': False, 'id': 1, 'depth': 0, 'name': 'Fake Article'}, -1: {'importance': 1, 'display_name': True, 'id': -1, 'depth': 0, 'name': 'Egypt'}, -8: {'importance': 1, 'display_name': True, 'id': -8, 'depth': 0, 'name': 'Libya'}, -7: {'importance': 1, 'display_name': True, 'id': -7, 'depth': 0, 'name': 'Ottoman Empire'}, -6: {'importance': 1, 'display_name': True, 'id': -6, 'depth': 0, 'name': 'Caliphate'}, -5: {'importance': 1, 'display_name': True, 'id': -5, 'depth': 0, 'name': 'Israel'}, -4: {'importance': 1, 'display_name': True, 'id': -4, 'depth': 0, 'name': 'Syria'}, -3: {'importance': 1, 'display_name': True, 'id': -3, 'depth': 0, 'name': 'Arabic language'}, -2: {'importance': 1, 'display_name': True, 'id': -2, 'depth': 0, 'name': 'Islam'}})
            
            # Type_Links_by_id
            articleconcept_type = {
                "id": 1, 
                "color": "#FFAAFF", 
                "node_ids": list(ArticleConcept.objects.values_list('id', flat=True)),
            }
            self.assertEqual(to_dict([articleconcept_type]),
                {1: {'id': 1, 'color': '#FFAAFF', 'node_ids': [1, 2, 3, 4, 5, 6, 7, 8]}})
            
            # Links_by_id
            self.assertEqual(to_dict(ArticleConcept.objects.all()), 
                {1: {'sourceID': 1, 'id': 1, 'targetID': -1, 'strengh': 0.95995, 'name': 'Fake Article <-0.95995-> Egypt'}, 2: {'sourceID': 1, 'id': 2, 'targetID': -2, 'strengh': 0.906098, 'name': 'Fake Article <-0.906098-> Islam'}, 3: {'sourceID': 1, 'id': 3, 'targetID': -3, 'strengh': 0.853767, 'name': 'Fake Article <-0.853767-> Arabic language'}, 4: {'sourceID': 1, 'id': 4, 'targetID': -4, 'strengh': 0.688198, 'name': 'Fake Article <-0.688198-> Syria'}, 5: {'sourceID': 1, 'id': 5, 'targetID': -5, 'strengh': 0.624983, 'name': 'Fake Article <-0.624983-> Israel'}, 6: {'sourceID': 1, 'id': 6, 'targetID': -6, 'strengh': 0.611671, 'name': 'Fake Article <-0.611671-> Caliphate'}, 7: {'sourceID': 1, 'id': 7, 'targetID': -7, 'strengh': 0.611542, 'name': 'Fake Article <-0.611542-> Ottoman Empire'}, 8: {'sourceID': 1, 'id': 8, 'targetID': -8, 'strengh': 0.57948, 'name': 'Fake Article <-0.57948-> Libya'}})
            print(to_json(ArticleConcept.objects.all()))
            

    def test_python_1(self):
        if False:
            from io import StringIO
            import json
            io = StringIO()
            json.dump({"a": [1]}, io)
            print(io.getvalue())