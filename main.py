# pip install spacy
# python -m spacy download en_core_web_sm

import spacy
from collections import Counter

from spacy.lang.fr.examples import sentences

#nlp = spacy.load('fr_core_news_sm')
nlp = spacy.load('fr')

# Process whole documents
f = open('output-onlinecsvtools.txt', encoding="utf8")

content = f.read()

f.close()

doc = nlp(content)

# all tokens that arent stop words or punctuations
words = [token.text for token in doc if token.is_stop != True and token.is_punct != True]

# noun tokens that arent stop words or punctuations
nouns = [token.text for token in doc if token.is_stop != True and token.is_punct != True and token.pos_ == "NOUN"]

# five most common tokens
word_freq = Counter(words)
common_words = word_freq.most_common(20)
print(common_words)

# five most common noun tokens
noun_freq = Counter(nouns)
common_nouns = noun_freq.most_common(20)
print(common_nouns)

# Find named entities, phrases and concepts
"""
for sentence in doc.sents:
    i = 0
    while i < len(common_nouns):
        for word in sentence:
            if word.text == common_nouns[i][0]:
                print(sentence)
        i += 1
"""

def print_best_phrase(w):
    for sentence in doc.sents:
        for word in sentence:
            if word.text == w:
                print(sentence)

print_best_phrase("chine")
