word = input("Enter a noun: ")

if word.endswith("y"):
    plural = word[:-1] + "ies"
elif word.endswith(("s", "x", "z", "ch", "sh")):
    plural = word + "es"
else:
    plural = word + "s"

print("Plural Form:", plural)
