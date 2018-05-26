from django.conf.urls import url
from django.contrib import admin

from .views import (
	pipeline_list,
	pipeline_create,
	pipeline_detail,
	pipeline_update,
	pipeline_delete,
	)

urlpatterns = [
	url(r'^$', pipeline_list, name='list'),
    url(r'^create/$', pipeline_create, name='create'),
    url(r'^(?P<slug>[\w-]+)/$', pipeline_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', pipeline_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', pipeline_delete, name='delete'),
    #url(r'^Pipelines/$', "<appname>.views.<function_name>"),
]
