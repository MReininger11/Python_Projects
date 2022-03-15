# Translator application that replaces vowels with the letter "g"

def translate(phrase):
    translation = ""
    for letter in phrase:                   # inspects each letter of "phrase" one at a time
        if letter in "AEIOUaeiou":          # compares individual letter against known vowels
            translation = translation + "g" # and returns "g" if vowel is detected
        else:
            translation = translation + letter  #if no vowel is detected, letter is returned
    return translation                          #to its original location unchanged

print(translate(input("Enter a phrase: ")))
