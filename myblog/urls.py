# encoding: utf-8
"""
@author: yousheng
@contact: 1197993367@qq.com
@site: http://youyuge.cn

@version: 1.0
@license: Apache Licence
@file: urls.py
@time: 17/9/5 下午3:35

"""
from django.conf.urls import url, include
import views

urlpatterns = [
    # 用r'^$'约束空字符串
    url(r'^index/$', views.blog),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page, name='edit_page'),
    url(r'^edit/action/$', views.edit_action, name='edit_action'),
]
