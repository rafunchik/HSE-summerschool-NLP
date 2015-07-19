# -*- coding: utf-8 -*-

import pymorphy2
from nltk.tokenize import RegexpTokenizer,wordpunct_tokenize
from nltk.corpus import stopwords

morph = pymorphy2.MorphAnalyzer()
p = morph.parse(u'стали')[0]
print p.tag

s = u'Пикабу, помоги! Почему стали тормозить даже игры, которые раньше шли вполне без зависаний, гуглим?'
tokenizer = RegexpTokenizer('\w+| \$ [\d \.]+ | S \+')
tokens1 = tokenizer.tokenize(s)
tokens2 = wordpunct_tokenize(s)

for t in tokens1:
    p = morph.parse(t)[0]
    print p.normal_form,'utf-8' 
#print tokens1
#print tokens2

import nltk
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()


input_path = '/Users/rcastro/Desktop/SU/data/alice.txt'
# 
with open(input_path,'r') as f:
    lines = f.readlines()
# 
text = ''    
for line in lines:
    text += line.decode('utf-8')
#
'''
tokens = WhitespaceTokenizer().tokenize(text)
print 'N of tokens:', len(tokens)
types = nltk.FreqDist(tokens)
print 'N of types:', len(types)
for i in types.most_common(20):
    print i
stems = nltk.FreqDist()
for t in types:
    s = stemmer.stem(t)
    if s in stems:
         stems[s] += types[t]
    else:
         stems[s] = types[t]
print 'N of stems:', len(stems)        
for i in stems.most_common(20):
    print i

lemmata = nltk.FreqDist()
for t in types:
    l = lemmatizer.lemmatize(t)
    if l in lemmata:
         lemmata[l] += types[t]
    else:
         lemmata[l] = types[t]
print 'N of lemmata:', len(lemmata)
stopwords = stopwords.words('english')
for i in lemmata.most_common(20):
    if i not in stopwords:
        print i
'''
    
article = u'''Last year Barclays launched their own fintech incubator and Santander set up a fund to invest in fintech companies, while this year Visa Europe has launched an accelerator called Collab. One of the first graduates of the Barclays accelerator is Aneesh Varma, co-founder of Aire, which provides an alternative credit score for consumers. He feels that joining a bank-backed incubator was the right thing for his business.
Funding aside, the most desirable currencies in the fintech sector are trust and credibility. Aneesh says: “Most of the financial ecosystem depends on common protocols. Having one bank as a ‘buddy’ gives you a head start over your competition and helps reassure clients and consumers that you’re okay to do business with.'''  
text = u"All good a friend is going to have a look for me tomorrow after work."

from nltk.tag import pos_tag

tokens1 = tokenizer.tokenize(article)
tokens2 = tokenizer.tokenize(text)

tags1 = pos_tag(tokens1)
tags2 = pos_tag(tokens2)


types = nltk.FreqDist(tags1)
types2 = nltk.FreqDist(tags2)
for x in types:
    print x
print types2




# import matplotlib.pyplot as plt
# fr = types.values()
# fr.sort(reverse=True)
# plt.plot(fr[:100])
# plt.ylabel('Type frequency')
# plt.xlabel('Type rank')
# plt.title("Zipf's law. First 100 types of 'Alice in Wonderland'")
# plt.show()
