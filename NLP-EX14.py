sentence = input("Enter sentence: ").split()

singular_subjects = {'he', 'she', 'ram'}
plural_subjects = {'they', 'we'}

if len(sentence) >= 2:
    subject = sentence[0].lower()
    verb = sentence[1].lower()

    if subject in singular_subjects and verb.endswith('s'):
        print("Agreement Correct")
    elif subject in plural_subjects and not verb.endswith('s'):
        print("Agreement Correct")
    else:
        print("Agreement Incorrect")
else:
    print("Invalid sentence")
