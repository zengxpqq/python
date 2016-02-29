#!/usr/bin/env python
# -*- coding: utf-8 -*-

from minicms1.wsgi import *
from news.models import Column, Article

def main():
	columns_urls = [
		('财经', 'financial'),
		('娱乐', 'entertainment'),
		('体育', 'sports'),
		('互联网', 'internet'),
		('时尚', 'fashion'),
		('汽车', 'car'),
		('军事', 'military'),
		('社会', 'society'),
		('科技', 'tech'),]

	for column_name, url in columns_urls:
		c = Column.objects.get_or_create(name=column_name, slug = url)[0]

		for i in range(1, 6):
			article = Article.objects.get_or_create(
				title = '{}_{}'.format(column_name, i),
				slug = 'article_{}'.format(i),
				content = '新闻详细内容： {} {}'.format(column_name, i)
			)[0]

			article.column.add(c)

if __name__ == '__main__':
	main()
	print("Done!")