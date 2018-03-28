import nltk
import string
import re
from collections import Counter
from nltk.corpus import stopwords    
from nltk.corpus import wordnet as wn

WORD_CLASS = {
    "n": "Noun",
    "v": "Verb",
    "a": "Adjective",
    "s": "Adjective Satellite",
    "r": "Adverb"
}

Trump_Tweet = ('THE SECOND AMENDMENT WILL NEVER BE REPEALED! As much as' 
' Democrats would like to see this happen, and despite the words yesterday'
' of former Supreme Court Justice Stevens, NO WAY. We need more Republicans'
' in 2018 and must ALWAYS hold the Supreme Court!')

results = []
more_stop_words = ["rt", '...',"'s", "n't", "’", "“", "”","''","``","i","amp","i","the","it","https"]
# Cleanse the data and remove stop words
Stop_Words = stopwords.words('english') + list(string.punctuation) + more_stop_words

def execute(tweet, count_all):
    # Tokenize into words the given tweet
    words = nltk.word_tokenize(tweet)

    Filtered_Words = [w.lower() for w in words if w.lower() not in Stop_Words and not w.startswith('//')]

    # Feature engineer Word_Count and Word_Class
    count_all.update(Filtered_Words)

def recording_results(count_all):
    file = open('result.txt', 'w')
    # Print out relevant results
    for word, count in count_all.most_common():
        Word_Class = get_word_class(word)
        row = [word, count, Word_Class]
        file.write(" ".join(str(e) for e in row)+"\n")
        print(row)

    file.close()

def get_word_class(word):
    # Initialize the Word Class variable
    Word_Class = None

    # Check if word exists in the data package
    if len(wn.synsets(word)) > 0:
        # Get word class
        Word_Class = wn.synsets(word)[0].pos()
        # Convert key to word class
        Word_Class = WORD_CLASS[Word_Class]
    else:
        pass
    
    return Word_Class

def top20(count_all):
    file = open('t20.txt', 'w')
    # Print out relevant results
    for word, count in count_all.most_common(20):
        Word_Class = get_word_class(word)
        row = [word, count, Word_Class]
        file.write(" ".join(str(e) for e in row)+"\n")
        print(row)

    file.close()

if __name__ == '__main__':
    count_all = Counter()
    tweets = open("tweets.txt", "r")
    for tweet in tweets:
        execute(tweet, count_all)

    #recording_results(count_all)
    top20(count_all)