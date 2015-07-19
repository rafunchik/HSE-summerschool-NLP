import nltk
from nltk.tokenize import WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tag import pos_tag
from string import punctuation
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
from nltk.text import TextCollection
from nltk.corpus import stopwords 
exclude = set(punctuation + '0123456789[]')


input_path = '/Users/rcastro/Desktop/SU/data/sif2.txt'

with open(input_path,'r') as f:
    lines = f.readlines()

text = ''    
collection = []
for line in lines:
    text += line.decode('utf-8')
    collection.append(''.join(ch for ch in line.decode('utf-8').lower() if ch not in exclude))
    

text = ''.join(ch for ch in text if ch not in exclude)

tokens = WhitespaceTokenizer().tokenize(text.lower())
types = nltk.FreqDist(tokens) 


######### NOUNS EXTRACTION ######### 
# nouns =  nltk.FreqDist()
# 
# tags = pos_tag(types.keys())
# for t in tags:
#     if t[1] == 'NN':
#         nouns[t[0]] = types[t[0]]
#         
# for n in nouns.most_common(20): 
#     print n


######### ######### #########  ######### 


######### PATTTERN EXTRACTION (1) ######### 
# pattern_coll2  = nltk.FreqDist()
# 
# coll2 = nltk.FreqDist(nltk.bigrams(tokens))
# for c2 in coll2:
#     tags = pos_tag(c2)
#     if (tags[0][1] == 'JJ' and tags[1][1] == 'NN') or (tags[0][1] == 'NN' and tags[1][1] == 'NN'):
#         pattern_coll2[c2] = coll2[c2]
#         
#         
# for c2 in pattern_coll2.most_common(20):
#     print c2     
######### ######### ######### #########     

######### PATTTERN EXTRACTION (2) ######### 
# pattern_coll3  = nltk.FreqDist()
# 
# coll3 = nltk.FreqDist(nltk.ngrams(tokens, 3))
# for c3 in coll3:
#     tags = pos_tag(c3)
#     if tags[0][1] == 'JJ' and tags[1][1] == 'NN' and tags[2][1] == 'NN':
#         pattern_coll3[c3] = coll3[c3]
#         
#         
# for c3 in pattern_coll3.most_common(20):
#     print c3
######### ######### ######### #########     


######### BIGRAM ASSOCIATION  ######### 
# finder = BigramCollocationFinder.from_words(tokens)
# finder.apply_freq_filter(3)
# for i in finder.nbest(bigram_measures.pmi, 20): print ' '.join(i).encode('utf8')
######### ######### ######### #########

 
######### TF IDF  ASSOCIATION  ######### 
buf = []
collection = [WhitespaceTokenizer().tokenize(text) for text in collection]
corpus = TextCollection(collection)
for i in set(collection[0]):
    if not i in stopwords.words('english'):
        buf.append([ i, corpus.tf_idf(i, collection[6])])
for i in sorted(buf,key=lambda l:l[1], reverse=True)[:20]:
    print i

