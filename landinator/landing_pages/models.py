from django.db import models
from django.shortcuts import resolve_url as r
from django_extensions.db.fields import AutoSlugField


class LandingPage(models.Model):
    title = models.CharField('título', max_length=150)
    slug = AutoSlugField('slug', populate_from='title')
    end_date = models.DateField('vigente até')
    limit_subscriptions = models.IntegerField(
        'limite de inscrições', default=0)
    created_at = models.DateTimeField('criado em', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return r('home', slug=self.slug)
