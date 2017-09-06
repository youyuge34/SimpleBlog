# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')  # 要和model里的字段一致
    list_filter = ('pub_time',)


admin.site.register(Article, ArticleAdmin)
