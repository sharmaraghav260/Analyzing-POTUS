import nltk
import string
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

def execute():
    # Tokenize into words the given tweet
    words = nltk.word_tokenize(Trump_Tweet)

    # Cleanse the data and remove stop words
    Stop_Words = stopwords.words('english') + list(string.punctuation)

    Filtered_Words = [w for w in words if w not in Stop_Words]

    # Feature engineer Word_Count and Word_Class
    Word_Counter = Counter(Filtered_Words)

    # Print out relevant results
    for word, count in Word_Counter.most_common():
        Word_Class = get_word_class(word)
        row = [word, count, Word_Class]
        print(row)

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

if __name__ == '__main__':
    execute()