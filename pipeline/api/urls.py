from django.conf.urls import url
from django.contrib import admin

from .views import (
    PipelineDetailAPIView,
    PipelineUpdateAPIView,
    PipelineListAPIView,
    )

urlpatterns = [
    url(r'^$', PipelineListAPIView.as_view(), name='thread'),
    # url(r'^create/$', PipelineCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/$', PipelineDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', PipelineUpdateAPIView.as_view(), name='update')
]
