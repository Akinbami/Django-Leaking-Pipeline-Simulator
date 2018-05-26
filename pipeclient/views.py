from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from pipeline.models import Pipeline

User = get_user_model()
@login_required
def home(request):
	users = User.objects.all()
	leaking_pipelines = Pipeline.objects.filter(is_damaged='LEAKING')
	context = {
		"users": users,
		"leaking_pipelines": leaking_pipelines,
	}

	return render(request,'analysis.html',context)