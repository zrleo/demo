# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('标题', max_length=20)
    content = models.TextField('内容')
    publish_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:

        ordering = ['-publish_time']
