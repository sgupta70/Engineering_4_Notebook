
import time
#These are all the letters and numbers translated
MORSE_CODE = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '/':'-..-.', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
while True:
    user_input = input("Enter the string to translate, or type '-q' to quit. ") #prints out a space for you to type words in moniter
    user_input = user_input.upper()
    if user_input == "-X":
        break #everything stops if you type -x in
    morse_translation = ""
    translation_good = True
    for letter in user_input:
        if letter == " ":
            morse_translation += "/" #if you put a space it will make a break 
        else:
            try:
                morse_translation += MORSE_CODE[letter] + " "
            except KeyError:
                print(f"Unsupported character \"{letter}\" used. Please try again.") #if you put in a letter that can't work it will tell you
                translation_good = False
                break
    if translation_good:
        print(morse_translation) 
            
print("done")