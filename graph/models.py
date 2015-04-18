from django.db import models

class Website(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    rss_url = models.CharField(max_length=255)
