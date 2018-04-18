# -*- coding: utf-8 -*-
from django.contrib import admin
from myblog.models import Article
from pagedown.widgets import AdminPagedownWidget
from django import forms
# Register your models here.

# Register your models here.
# 定义自己的form
class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget(), required=False,label='')

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm

admin.site.register(Article,ArticleAdmin)
#admin.site.register(Article)
