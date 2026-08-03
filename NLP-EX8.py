tags = {
    "Ram":"NNP",
    "plays":"VBZ",
    "playing":"VBG",
    "is":"VBZ",
    "cricket":"NN",
    "good":"JJ"
}

sentence = input("Enter a sentence: ")

words = sentence.split()

print("POS Tags:")

for word in words:
    print(word,"->",tags.get(word,"NN"))
