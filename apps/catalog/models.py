from django.db import models
from django.core.urlresolvers import reverse
from django.shortcuts import render
import os
from django.conf import settings

# Create your models here.

class Logos(models.Model):
	"""
	公司logo
	"""
	title = models.CharField("公司名称",max_length=200)
	image_url = models.ImageField("图片路径",upload_to="logo/%Y/%m/%d",blank=True)
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
	callback_url = models.URLField('回调url',blank=True)
	image_url = models.ImageField('图片路径',upload_to='ad/%Y/%m/%d',blank=True)
	date_publish = models.DateTimeField('添加日期',auto_now_add=True)
	play = models.BooleanField('是否显示',default=False)
	index = models.IntegerField('排列顺序（从小到大）',default=999)

	class Meta:
		verbose_name = '首页广告'
		verbose_name_plural = verbose_name
		ordering = ['index','id']

	def get_image_url(self):
		self.url = str(self.image_url)
		return os.path.join(settings.MEDIA_URL,self.url)

	def __str__(self):
		return self.name

class Brand(models.Model):
	"""
	商品品牌
	"""
	name = models.CharField('品牌名称',max_length=100)
	slug = models.SlugField('品牌标签',max_length=100)
	description = models.TextField('品牌描述')
	index = models.IntegerField('排列顺序（从小到大）',default=999)

	class Meta:
		verbose_name = '商品品牌'
		verbose_name_plural = verbose_name
		ordering = ['index','id']

	def __str__(self):
		return self.name

class Category(models.Model):
	"""
	商品分类名称
	"""
	name = models.CharField('分类名称',max_length=200,db_index=True)
	slug = models.SlugField('分类标签',max_length=200,db_index=True,unique=True)
	description = models.TextField('分类描述',blank=True)
	index = models.IntegerField('排列顺序（从小到大）',default=999)

	class Meta:
		verbose_name = '商品分类'
		verbose_name_plural = verbose_name
		ordering = ['index','id']

	def get_absolute_url(self):
		return reverse('shopsys:product_grid',args=[self.slug])

	def __str__(self):
		return self.name

class Product(models.Model):
	"""
	商品
	"""
	name = models.CharField('商品名称',max_length=200)
	slug = models.SlugField('商品标签',max_length=200)
	image_url = models.ImageField('图片路径',upload_to='product/%Y/%m/%d',blank=True)
	description = models.TextField('商品描述',blank=True)
	price = models.DecimalField('商品价格',max_digits=10,decimal_places=2)
	discount_price = models.DecimalField('打折价格',max_digits=10,decimal_places=2,blank=True)
	stock = models.PositiveIntegerField('商品货存')
	available = models.BooleanField('商品是否有效',default=True)
	created = models.DateTimeField('发布时间',auto_now_add=True)
	updated = models.DateTimeField('更新时间',auto_now=True)
	category = models.ForeignKey(Category,related_name='products',verbose_name='分类')
	brand = models.ManyToManyField(Brand,related_name='categorys',verbose_name='品牌')

	class Meta:
		verbose_name = '商品'
		verbose_name_plural = verbose_name
		ordering = ['name']
		index_together = ['id','slug']

	def get_absolute_url(self):
		return reverse('shopsys:product_detail',args=[self.id, self.slug])

	def get_image_url(self):
		self.url = str(self.image_url)
		return os.path.join(settings.MEDIA_URL,self.url)

	def __str__(self):
		return self.name



