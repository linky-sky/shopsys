from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.conf import settings
from apps.catalog.models import *
from apps.cart.forms import CartAddProductForm
from apps.cart.cart import Cart

# Create your views here.

def global_setting(request):
	site_manager = settings.SITE_MANAGER
	site_manager['logo'] = Logos.objects.get(pk=1)
	site_manager['ads'] = Ads.objects.filter(play=True)
	site_manager['categorys'] = Category.objects.all()[:6]
	site_manager['more_categorys'] = Category.objects.all()[6:]
	site_manager['muying'] = Category.objects.get(slug='baby')
	site_manager['baby'] = Product.objects.filter(category=site_manager['muying'])
	site_manager['cart'] = Cart(request)
	return site_manager


def index(request):
	return render(request,'web/index.html',locals())


def product_detail(request,id,slug):
	product = get_object_or_404(Product,id=id,slug=slug,available=True)
	cartaddproductform = CartAddProductForm()
	return render(request,'web/detail.html',locals())


def product_grid(request,category_slug=None):
	category = None
	grid = True
	categories = Category.objects.all()
	products = Product.objects.filter(available=True)
	if category_slug:
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	if grid:
		return render(request,'web/product_grid.html',locals())
	else:
		return render(request,'web/product_list.html',locals())






