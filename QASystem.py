from ParsingFuncs import *
from QueryingFuncs import *
from RankingFuncs import *
import webbrowser

questionText = raw_input('Ask Away\n');

questionTokens = getNouns(questionText);
query = formulateQuery(questionTokens);
print 'QUERY N: \"', query, '\" \n';
titles = wikipedia.search(query, 3);

questionTokens = getNounsVerbs(questionText);
query = formulateQuery(questionTokens);
print 'QUERY NV: \"', query, '\" \n';

titles += wikipedia.search(query, 3);


print "TITLES: ", titles, "\n";

articles = getArticles(titles);
#print 'UPDATED TITLES: ', titles, '\n';


contents = getContents(articles);

contents = stemTokenListList(contents);
keyTokens = stemTokenList(questionTokens);

#print contents;
print keyTokens;

bestIndex = bestArticle(contents, keyTokens);

pageName = titles[bestIndex];

addressName = pageName.replace(' ', '_')
print addressName;

webbrowser.open('https://en.wikipedia.org/wiki/'+addressName);



