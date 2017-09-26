# coding=utf-8
from __future__ import unicode_literals
from django.db import models

from myDjango.settings import MEDIA_ROOT


# Create your models here.

class User(models.Model):
    u_name = models.CharField(u'姓名', max_length=255, null=True, blank=True)
    u_age = models.IntegerField(u'年龄', null=True, blank=True)
    u_sex = models.BooleanField(u'性别', default=True)
    u_position = models.CharField(u'职位', max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = "用户"

    def __unicode__(self):
        return self.u_name


class Article(models.Model):
    article_author = models.ForeignKey(User, verbose_name='用户', blank=True)
    title = models.CharField(max_length=255, verbose_name='标题', blank=True)
    desprition = models.CharField(verbose_name='简介', max_length=255, blank=True)
    image = models.ImageField(u'配图', blank=True)
    content = models.TextField(u'内容', blank=True)
    createtime = models.DateTimeField(verbose_name=u'时间', auto_now_add=True)

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'

    def __unicode__(self):
        return '%s' % (self.title)


class FileUpload(models.Model):
    file_name = models.CharField(max_length=255, null=True, blank=True)
    file_path = models.FileField(max_length=255, blank=True, upload_to=MEDIA_ROOT)

    class Meta:
        verbose_name = '文件'
        verbose_name_plural = '文件'

    def __unicode__(self):
        return '%s' % (self.file_name)
