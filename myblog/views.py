# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models

def blog(request):
    articles = models.Article.objects.all()
    return render(request,'myblog/index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk = article_id)
    return render(request,'myblog/article_page.html',{'article':article})