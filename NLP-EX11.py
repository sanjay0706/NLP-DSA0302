grammar = {
    'S': [['NP', 'VP']],
    'NP': [['Ram']],
    'VP': [['runs']]
}

sentence = input("Enter sentence: ").split()

def parse(symbol, words):
    if symbol not in grammar:
        return words and words[0] == symbol and len(words) == 1

    for rule in grammar[symbol]:
        if len(rule) == len(words):
            valid = True
            for s, w in zip(rule, words):
                if not parse(s, [w]):
                    valid = False
            if valid:
                return True
    return False

if parse('S', sentence):
    print("Accepted")
else:
    print("Rejected")
