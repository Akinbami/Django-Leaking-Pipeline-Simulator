# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PipelineForm,PipelineUpdateForm
from .models import Pipeline

@login_required
def pipeline_create(request):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
		
	form = PipelineForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		print "hello"
		print form
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()
		# message success
		messages.success(request, "Successfully Created")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
	}

	return render(request, "pipeline_create.html", context)

# Create your views here.
@login_required
def pipeline_detail(request, slug=None):
	instance = get_object_or_404(Pipeline, slug=slug)
	form = PipelineUpdateForm(request.POST or None, request.FILES or None, instance=instance)
	# print form.errors
	if form.is_valid():
		print 'very good'
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form": form,
		"instance": instance,
	}
	return render(request, "pipeline_detail.html", context)

@login_required
def pipeline_list(request):
	queryset_list = Pipeline.objects.all() #.order_by("-timestamp")
	if request.user.is_staff or request.user.is_superuser:
		queryset_list = Pipeline.objects.all()
	
	query = request.GET.get("q")
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)


	context = {
		"pipelines": queryset, 
		"title": "List",
		"page_request_var": page_request_var,
		# "today": today,
	}
	return render(request, "pipeline_list.html", context)

@login_required
def pipeline_update(request, slug=None):
	# if not request.user.is_staff or not request.user.is_superuser:
	# 	raise Http404
	instance = get_object_or_404(Pipeline, slug=slug)
	form = PipelineForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "<a href='#'>Item</a> Saved", extra_tags='html_safe')
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "pipeline_form.html", context)


@login_required
def pipeline_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Pipeline, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	return redirect("pipelines:list")
