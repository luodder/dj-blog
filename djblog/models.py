# -*- coding: utf-8 -*-

from django.db import models

class Article(models.Model):
    STATUS_CHOICE = (
        ('d','Draft'),
        ('p','Published'),
    )

    title = models.CharField(u'标题',max_length=70)
    body = models.TextField(u'正文')
    create_time = models.DateField(u'创建时间', auto_now_add=True)
    last_modified_time = models.DateField(u'修改时间', auto_now_add=True)
    status = models.CharField(u'文章状态',max_length=1,choices=STATUS_CHOICE)
    abstract = models.CharField(u'摘要',max_length=54, blank=True, null=True,help_text="可选，如若为空讲摘取正文的前54个字符")

    views = models.PositiveIntegerField(u'浏览量', default=0)
    likes = models.PositiveIntegerField(u'点赞数', default=0)
    topped = models.BooleanField(u'置顶', default=False)

    category = models.ForeignKey('Category', verbose_name='分类', null= True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-last_modified_time']

class Category(models.Model):

    name = models.CharField('类名', max_length=20)
    create_time = models.DateField(u'创建时间',auto_now_add=True)
    modified_time = models.DateField(u'修改时间',auto_now_add=True)

    def __str__(self):
        return self.name
