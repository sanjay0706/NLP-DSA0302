import nltk
from nltk.tokenize import word_tokenize

text = input("Enter a sentence: ")

words = word_tokenize(text)

tags = nltk.pos_tag(words)

print(tags)
