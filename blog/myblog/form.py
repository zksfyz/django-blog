from models import Article
from pagedown.widgets import AdminPagedownWidget
from django import forms

class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=AdminPagedownWidget(), required=False,label='')

    class Meta:
        model = Article
	fields = '__all__'
