from django.contrib import admin
from apps.catalog.models import *
# Register your models here.


class AdsAdmin(admin.ModelAdmin):
	class Media:
		js = (
			'/static/kindeditor-4.1.10/kindeditor-min.js',
			'/static/kindeditor-4.1.10/lang/zh_CN.js',
			'/static/kindeditor-4.1.10/config.js',
			)

	search_fields = ['title']
	list_display = ['name','title','date_publish']
	list_filter = ['play','date_publish']


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','slug','index']
	prepopulated_fields = {'slug':['name']}


class ProductAdmin(admin.ModelAdmin):
	list_display = ['name','slug','price','discount_price','stock','available','created','updated']
	list_filter = ['available','created','updated']
	list_editable = ['price','stock','available']
	prepopulated_fields = {'slug':['name']}


admin.site.register(Logos)
admin.site.register(Ads,AdsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)