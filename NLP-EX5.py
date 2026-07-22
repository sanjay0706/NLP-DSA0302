import nltk
from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["playing", "running", "studies", "easily", "happiness"]

print("Original Words:")
print(words)

print("\nStemmed Words:")
for word in words:
    print(word, "->", ps.stem(word))
