# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .models import Column, Article 
from django.shortcuts import redirect

from news.forms import SearchForm

# Create your views here.

def index(request):

	home_display_columns = Column.objects.filter(home_display = True)
	nav_display_columns = Column.objects.filter(nav_display = True)

	#article = Article.objects.get(pk = 1)
	
	return render(request, 'index.html', {
		'home_display_columns': home_display_columns,
		'nav_display_columns': nav_display_columns,
	#	'article': article,
	})

def search(request):

	search = request.GET['search']
	searchcolumn = Column.objects.filter(name__icontains = search)

	for scolumn in searchcolumn:
		slugs = scolumn.slug

	searcharticle = Column.objects.get(slug = slugs)

        
	return render(request, 'index.html', {
		'searchcolumn': searchcolumn,
		'searcharticle': searcharticle,
	})
	
	

'''
def index(request):
	#columns = Column.objects.all()
	return HttpResponse('columns')
'''
def column_detail(request, column_slug):
	column = Column.objects.get(slug = column_slug)
	return render(request, 'news/column.html', {'column': column})

def article_detail(request, pk, article_slug):
	article = Article.objects.get(pk = pk)

	if article_slug != article.slug:
		return redirect(article, permanent = True)

	return render(request, 'news/article.html', {'article': article})

def home(request):
	return render(request, 'news/home.htm')
	#return HttpResponse('hhhhadksfj')

