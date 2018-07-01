l = raw_input("input a letter of the alphabet:")
if l in ('a','e','i','o','u'):
    print("%s is an vowel."%l)
elif l =='y':
    print("sometimes letter y stand for vowel,sometime for consonant.")
else:
    print("%s is a consonant" %l)
