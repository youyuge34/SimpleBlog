# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import models

def blog(request):
    articles = models.Article.objects.all()
    return render(request,'myblog/index.html',{'articles':articles})