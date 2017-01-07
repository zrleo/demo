# -*- coding:utf-8 -*-
from django.shortcuts import render

# Create your views here.

from django.http import  HttpResponse
from django.template import loader

from models import Article

def index(request):

        latest_article_list = Article.objects.order_by('-publish_time')
        template = loader.get_template('demo/index.html')
        context = {
            'latest_article_list': latest_article_list,
        }
        return HttpResponse(template.render(context, request))
