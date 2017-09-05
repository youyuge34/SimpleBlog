# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models


def blog(request):
    articles = models.Article.objects.all()
    return render(request, 'myblog/index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'myblog/article_page.html', {'article': article})


def edit_page(request, article_id):
    if str(article_id) == '0':
        return render(request, 'myblog/edit_page.html')
    else:
        article = models.Article.objects.get(pk=article_id)
        return render(request, 'myblog/edit_page.html', {'article': article})


def edit_action(request):
    """
    新增文章逻辑
    :param request:
    :return:
    """
    title = request.POST.get('title')  # 获取表单数据
    content = request.POST.get('content')
    article_id = request.POST.get('article_id', '0')  # 获取隐藏的文章id

    if article_id == '0':  # 新增文章逻辑
        models.Article.objects.create(title=title, content=content)
        articles = models.Article.objects.all()
        return render(request, 'myblog/index.html', {'articles': articles})
    else:  # 修改文章逻辑
        article = models.Article.objects.get(pk=article_id)
        article.title = title
        article.content = content
        article.save()
        return render(request, 'myblog/article_page.html', {'article': article})
