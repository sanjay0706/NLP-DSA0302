sentence = input("Enter a sentence: ")

words = sentence.split()

for word in words:

    tag = "NN"

    if word.lower() in ["is","am","are","was","were"]:
        tag = "VB"

    elif word.endswith("ing"):
        tag = "VBG"

    elif word.endswith("ed"):
        tag = "VBD"

    print(word,"->",tag)
