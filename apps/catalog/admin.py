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


admin.site.register(Logos)
admin.site.register(Ads,AdsAdmin)