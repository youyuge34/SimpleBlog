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


def edit_page(request):
    return render(request, 'myblog/edit_page.html')


def edit_action(request):
    """
    新增文章逻辑
    :param request:
    :return:
    """
    title = request.POST.get('title')
    content = request.POST.get('content')
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    return render(request, 'myblog/index.html', {'articles': articles})
