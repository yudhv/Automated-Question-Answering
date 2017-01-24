#Module: QueryingFuncs.py

import nltk
import numpy
import wikipedia
from nltk import *
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from ParsingFuncs import *
from RankingFuncs import *

def printFreqDists(articles, freqDists):
	for i in range(0, len(articles)):
		print articles[i], ' :  ';
		print freqDists[i].tabulate(), '\n';


def delDisambs(titles):
	disambiguation = '(disambiguation)';
	for title in titles:
		if disambiguation in title:
			titles.remove(title);

def getTitlesFor(question, count):
	allTitles = [];
	for token in question:
		titles = wikipedia.search(token, results=count, suggestion=False);
		allTitles.append(titles);
	return allTitles;

def getArticles(titles):
	articles = [];
	dPgs = [];
	for title in titles:
		try: 
			article = wikipedia.page(title=title, redirect=True);
		except:
			dPgs.append(title);
		else:
			articles.append(article);
	[titles.remove(title) for title in dPgs]
#	print 'UPDATED TITLES (INFUNC): ', titles, '\n';
	return articles;

def getContents(articles):
	contents = [];
	for article in articles:
		content = article.content;
		content = content.lower();
		content = content.split();
		contents.append(content);
	return contents;


		

