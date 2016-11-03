# etd_ngrams.py
# Python script for generating ngrams from the UNM electronic theses and dissertation
# title and abstracts extracted from http://repository.unm.edu in 2016-10. 

import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords

stop = set(stopwords.words('english'))
punctuation = ".,;:()'\"[]{}?!=/"
n = [1,2,3]

inputFile = open('abstracts.txt', 'r')

text = inputFile.read()
inputFile.close()

tokens = nltk.word_tokenize(text.decode('utf8'))
filteredTokens = [w.lower() for w in tokens if not w.lower() in stop]
depunctuatedTokens = [w for w in filteredTokens if not w in punctuation]

for thisN in n:
	outFileName = "_".join([str(thisN),"grams.txt"])
	outFile = open(outFileName,'w')
	
	thisgram = ngrams(depunctuatedTokens,thisN)

	fdist = nltk.FreqDist(thisgram)

	for item in fdist.items():
		outputString =  '\t'.join([' '.join(item[0]),str(item[1]),'\n'])
		print outputString
		outFile.write(outputString.encode('utf8'))
	
	outFile.close()

