from django.db import models

# Create your models here.

class Logos(models.Model):
	"""
	公司logo
	"""
	title = models.CharField("公司名称",max_length=200)
	image_url = models.ImageField("图片路径",upload_to="logo/%Y%m%d")
	description = models.CharField('描述',max_length=200)
	play = models.BooleanField("是否显示",default=False)

	class Meta:
		verbose_name = '公司logo'
		verbose_name_plural = verbose_name
		ordering = ['id']

	def __str__(self):
		return self.title


class Ads(models.Model):
	"""
	首页广告
	"""
	name = models.CharField('广告主题',max_length=100)
	title = models.CharField('广告标题',null=True,blank=True,max_length=200)
	description = models.TextField('广告描述',null=True,blank=True)
	callback_url = models.URLField('回调url',null=True,blank=True)
	image_url = models.ImageField('图片路径',upload_to='ad/%Y%m%d')
	date_publish = models.DateTimeField('添加日期',auto_now_add=True)
	play = models.BooleanField('是否显示',default=False)
	index = models.IntegerField('排列顺序（从小到大）',default=999)

	class Meta:
		verbose_name = '首页广告'
		verbose_name_plural = verbose_name
		ordering = ['index','id']

	def __str__(self):
		return self.name