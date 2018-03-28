import nltk
import string
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

# Tokenize into words the given tweet
words = nltk.word_tokenize(Trump_Tweet)

# Cleanse the data and remove stop words
Stop_Words = stopwords.words('english') + list(string.punctuation)

Filtered_Words = [w for w in words if w not in Stop_Words]

print(Filtered_Words)