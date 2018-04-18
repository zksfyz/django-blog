#-*-coding:utf-8-*-
from __future__ import unicode_literals 
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
@python_2_unicode_compatible
class Article(models.Model) :
    GENDER_CHOICES = (
        (u'Django', u'Django'),
        (u'Python', u'Python'),
        (u'运维', u'运维'),
        (u'网络', u'网络'),
        (u'安全', u'安全'),
        (u'Java', u'Java'),
        (u'Linux', u'Linux'),
        (u'Centos', u'Centos'),
        (u'Shell', u'Shell'),
        (u'Web', u'Web'),
        (u'Nginx', u'Nginx'),
        (u'uwsgi', u'uwsgi'),
        (u'Oracle', u'Oracle'),
        (u'Mysql', u'Mysql'),
        (u'MongoDB', u'MongoDB'),
        (u'Redis', u'Redis'),
        (u'开源', u'开源'),
        (u'PHP', u'PHP'),
        (u'其他', u'其他'),
    )
    title = models.CharField(max_length = 100)  #博客题目
    category = models.CharField(max_length = 50, choices=GENDER_CHOICES)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)  #博客日期
    content = models.TextField(blank = True, null = True)  #博客文章正文
    file_url = models.FileField(upload_to = './uploads/',blank=True,null=True,default='')
    def get_absolute_url(self):
	path = reverse('detail',kwargs={'id':self.id})
	return "http://www.zksfyz.com%s"%(path)

    #python2使用__unicode__, python3使用__str__
    def __str__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']
