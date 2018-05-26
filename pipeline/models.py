# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.safestring import mark_safe
from django.utils.text import slugify

from .choices import *



def upload_location(instance, filename):
    PipelineModel = instance.__class__
    # new_id = PipelineModel.objects.order_by("name").last().id + 1
    return "%s" %(filename)

class Pipeline(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    longitude = models.DecimalField(max_digits=100, decimal_places=6)
    latitude = models.DecimalField(max_digits=100, decimal_places=6)
    is_damaged = models.CharField(max_length=100, choices=DAMAGE_STATUS_CHOICES, default='NOT Leaking')
    damage_grade = models.CharField(max_length=100, choices=LEAK_GRADE, default='None') 
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # objects = PipelineManager()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pipelines:detail", kwargs={"slug": self.slug})

    def get_api_url(self):
        return reverse("pipeline-api:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-timestamp", "-updated"]

    


def create_slug(instance, new_slug=None):
    slug = slugify(instance.name)
    if new_slug is not None:
        slug = new_slug
    qs = Pipeline.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_pipeline_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_pipeline_receiver, sender=Pipeline)










