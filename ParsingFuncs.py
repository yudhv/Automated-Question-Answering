#Module: ParsingFuncs.py

import nltk
import numpy
import wikipedia
from nltk import *
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def delStops(text):	
	engStops = stopwords.words('english');
	stops = [];
	for word in text:
		if word.lower() in engStops:
			stops.append(word);
	for word in stops:
		text.remove(word);
	return text;

def lowerCaseList(list):
	lowerList = [];
	for element in list:
		lowerList.append(element.lower());
	return lowerList;

def formulateQuery(quesTokens):
	query = '';
	for token in quesTokens:
		query += token;	
		query += ' ';
	return query;
		
def extractQuesNounVerbFocus(tokens):
	taggedTokens = nltk.pos_tag(tokens);
#	print 'POS TAGS OF QUESTION: ', taggedTokens;
	focus = [];
	for tuple in taggedTokens:			
		if tuple[1] in ['CD', 'FW', 'NN', 'NNS', 'NNP', 'NNPS', 'VB', 'VBD', 'VBG', 'VBN', 'VBZ', 'VBP']:
			focus.append(tuple[0]);
			
	if len(focus)>0:
		return focus;
	else:
		return tokens;

def extractQuesNounFocus(tokens):
	taggedTokens = nltk.pos_tag(tokens);
#	print 'POS TAGS OF QUESTION: ', taggedTokens;
	focus = [];
	for tuple in taggedTokens:			
		if tuple[1] in ['CD', 'FW', 'NN', 'NNS', 'NNP', 'NNPS']:
			focus.append(tuple[0]);
			
	if len(focus)>0:
		return focus;
	else:
		return tokens;
	
	
def parseQuestion(question):
	words = question.split();
	tokens = [];
	[tokens.append(word) for word in words if word not in tokens];
	print 'TOKENS: ', tokens; 
	question = delStops(tokens);
	quesFocus = extractQuesFocus(question);
	print 'QUESTION: ', question;
	print 'QUESTION FOCUS: ', quesFocus;
	return quesFocus;

def parseQuestionNouns(question):
	words = question.split();
	tokens = [];
	[tokens.append(word) for word in words if word not in tokens];
	print 'TOKENS: ', tokens; 
	question = delStops(tokens);
	quesFocus = extractQuesNounFocus(question);
	print 'QUESTION: ', question;
	print 'QUESTION NOUN FOCUS: ', quesFocus;
	return quesFocus;


def stemTokenList(list):
	list = lowerCaseList(list);
	stemmer = PorterStemmer();
	stems = [];
	for word in list:
		stem = stemmer.stem(word);
		stems.append(stem);
	return stems;

def stemTokenListList(lists):
	stemmer = PorterStemmer();
	stemsList = [];
	for list in lists:
		list = lowerCaseList(list);
		stems= [];
		for word in list:
			stem = stemmer.stem(word);
			stems.append(stem);
		stemsList.append(stems);
	return stemsList;


def getNouns(question):
	words = question.split();
	tokens = [];
	[tokens.append(word) for word in words if word not in tokens];
#	print 'QUESTION TOKENS: ', tokens; 
	question = delStops(tokens);
	quesFocus = extractQuesNounFocus(question);
#	print 'QUESTION: ', question;
	print 'NOUNS: ', quesFocus;
	return quesFocus;

def getNounsVerbs(question):
	words = question.split();
	tokens = [];
	[tokens.append(word) for word in words if word not in tokens];
#	print 'QUESTION TOKENS: ', tokens; 
	question = delStops(tokens);
	quesFocus = extractQuesNounVerbFocus(question);
#	print 'QUESTION: ', question;
	print 'NOUNS & VERBS: ', quesFocus;
	return quesFocus;
	