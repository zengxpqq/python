# -*- coding: utf-8 -*-

from django import forms

# Create your views here.

class SearchForm(forms.Form):
	search = forms.CharField()


