
# coding: utf-8

# In[1]:

# Python script for generating ngrams from the UNM electronic theses and dissertation
# title and abstracts extracted from http://repository.unm.edu in 2016-10. 


# In[20]:

import nltk
from nltk.util import ngrams
from nltk.corpus import stopwords
from operator import itemgetter


# In[45]:

stop = set(stopwords.words('english'))
punctuation = set(u".,;:()'\"[]{}<>?!=/#%&$12345678910".decode('utf8'))
annoyances = set({u'``',u"''",u'\x9d',u"'s"})
longstoplist = {}
awl = {}

with open('longstoplist.txt','r') as infile:
    listtext = nltk.word_tokenize(infile.read().decode('utf8').lower())
    longstoplist = set(listtext)
with open('AWL.txt','r') as infile:
    listtext = nltk.word_tokenize(infile.read().decode('utf8').lower())
    awl = set(listtext)

fullstop = sorted((stop | punctuation | longstoplist | awl | annoyances), key=itemgetter(0))
totalStopWords = len(stop) + len(punctuation) + len(longstoplist) + len(awl) + len(annoyances)

with open('fullStopWords.txt','w') as outfile:
    for word in fullstop:
        #print word
        outfile.write(word.encode("UTF-8")+"\n")
    

print "Total words in the separate source lists: " + str(totalStopWords)
print "Total unique stop words in the combined list: " + str(len(fullstop))


# In[46]:

n = [1,2,3,4]
xgrams = []

with open('abstracts.txt', 'r') as infile:
    tokens = nltk.word_tokenize(infile.read().decode('utf8'))
    filteredTokens = [w.lower() for w in tokens if not w.lower() in fullstop]
    for thisN in n:
        thisgram = ngrams(filteredTokens,thisN)
        fdist = sorted(nltk.FreqDist(thisgram).items(),key=itemgetter(1), reverse=True) 
        xgrams.extend([[thisN,fdist]])


# In[47]:

for xgram in xgrams:
    thisN = xgram[0]
    outFileName = "_".join([str(thisN),"grams.txt"])
    with open(outFileName, 'w') as outFile:
        for item in xgram[1]:
            outputString =  '\t'.join([' '.join(item[0]),str(item[1]),'\n'])
            # print outputString
            outFile.write(outputString.encode('utf8'))            


# In[ ]:





# In[ ]:




# In[ ]:



