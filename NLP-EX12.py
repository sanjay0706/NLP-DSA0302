import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

grammar = CFG.fromstring('''
S -> NP VP
NP -> 'Ram'
VP -> 'runs'
''')

parser = EarleyChartParser(grammar)

sentence = "Ram runs".split()

for tree in parser.parse(sentence):
    print(tree)
