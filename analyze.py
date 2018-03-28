import nltk
from collections import Counter
from nltk.corpus import stopwords    
from nltk.corpus import wordnet as wordnet

WORD_CLASS = {
    "n": "Noun",
    "v": "Verb",
    "a": "Adjective",
    "r": "Adverb"
}

Trump_Tweet = ('THE SECOND AMENDMENT WILL NEVER BE REPEALED! As much as' 
' Democrats would like to see this happen, and despite the words yesterday'
' of former Supreme Court Justice Stevens, NO WAY. We need more Republicans'
' in 2018 and must ALWAYS hold the Supreme Court!')

# Tokenize the Words in the tweet
words = nltk.word_tokenize(Trump_Tweet)

print(words)