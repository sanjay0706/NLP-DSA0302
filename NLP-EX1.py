import re

text = input("Enter a sentence: ")
pattern = input("Enter pattern to search: ")

match = re.search(pattern, text)

if match:
    print("Pattern Found")
    print("Matched Word:", match.group())
else:
    print("Pattern Not Found")
