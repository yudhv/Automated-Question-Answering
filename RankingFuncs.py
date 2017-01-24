#Module: RankingFuncs.py

import nltk
import numpy
import wikipedia
from nltk import *
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def keyFreqDists(keywords, contents):
	freqDists = getFreqDists(contents);
	keyFreqs = retainKeyFreqs(keywords, freqDists);
	return keyFreqs;

def getFreqDists(texts):
	freqDists = [];
	for text in texts:
		freqDist = FreqDist(text);
		freqDists.append(freqDist);
	return freqDists;

def retainKeyFreqs(keywords, freqDists):
	keyFreqs = freqDists;
	for freqDist in keyFreqs:
		words = freqDist.keys();
		for word in words:
			if word not in keywords:
				del freqDist[word];
	return keyFreqs;

def printFreqDists(names, freqDists):
	for i in range(0, len(names)):
		print names[i], ' :  ';
		print freqDists[i].tabulate();

def getAggregateFreqs(contentStems, quesStems):
	counts = [];
	for text in contentStems:
		count = 0;
		for word in quesStems:
			count += text.count(word);
		counts.append(count);
	print "getAggFreqs", counts;
	return counts;
					
def bestArticle(contents, keyTokens):
	weights = [];
	for content in contents:
		weight = 0;
		for token in keyTokens:
#			print token, ' ', content.count(token);
			weight += content.count(token);
		weights.append(weight);
	print weights;

	maxWeight = 0;
	maxIndex = 0;
	for index in range( 0, len(weights) ):
		if weights[index] > maxWeight:
			maxWeight = weights[index];
			maxIndex = index;
	return maxIndex;
		

