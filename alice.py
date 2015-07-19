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
    print p.tag
    
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


from nltk.tag import pos_tag
pos_tag(['ship'])



# import matplotlib.pyplot as plt
# fr = types.values()
# fr.sort(reverse=True)
# plt.plot(fr[:100])
# plt.ylabel('Type frequency')
# plt.xlabel('Type rank')
# plt.title("Zipf's law. First 100 types of 'Alice in Wonderland'")
# plt.show()
