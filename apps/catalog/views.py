from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.conf import settings
from apps.catalog.models import *
# Create your views here.

def global_setting(request):
	site_manager = settings.SITE_MANAGER
	site_manager['logo'] = Logos.objects.get(pk=1)
	site_manager['ads'] = Ads.objects.filter(play=True)
	return site_manager


def index(request):
	return render(request,'web/index.html',locals())