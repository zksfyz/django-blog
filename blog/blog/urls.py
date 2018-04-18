# -*- coding:utf-8 -*-
"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from myblog import views as blog
from django.conf.urls import handler404,handler500
import os
from django.views.static import serve as staticserve

handler404 = "myblog.views.page_not_found"
handler500 = "myblog.views.page_error"

urlpatterns =[
    url(r'^admin/', admin.site.urls),
    #url(r'^(?P<id>\d+)/$',views.detail),
    url(r'^(?P<id>\d+)/$', blog.detail, name='detail'),
    url(r'^$',blog.home,name='home'),
    url(r'^archives/$', blog.archives, name = 'archives'),
    url(r'^aboutme/$', blog.about_me, name = 'about_me'),
    url(r'^tag(?P<tag>\w+)/$', blog.search_tag, name = 'search_tag'),
    url(r'^search/$',blog.blog_search, name = 'search'),
    #url(r'^media/[^/]$',blog.file_download,name = 'download'),
    #url(r'^downloads/$',blog.downloads,name = 'downloads'),
    #url(r'^404page$', 'myblog.views.error404', name='404page'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG404:
    urlpatterns += [ 
        url(r'^media/(?P<path>.*)$', staticserve, { 'document_root': settings.MEDIA_ROOT, }), url(r'^static/(?P<path>.*)$', staticserve, { 'document_root': settings.STATIC_ROOT }),
    ]


#handler404 = "myblog.views.page_not_found"
#handler500 = "myblog.views.page_error"
