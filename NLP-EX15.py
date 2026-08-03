import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

grammar = PCFG.fromstring('''
S -> NP VP [1.0]
NP -> 'Ram' [0.5] | 'apples' [0.5]
VP -> 'eats' NP [1.0]
''')

parser = ViterbiParser(grammar)

sentence = "Ram eats apples".split()

for tree in parser.parse(sentence):
    print(tree)
