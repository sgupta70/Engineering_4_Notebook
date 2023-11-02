#type: ignore

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP1) #where the LED is connected
led.direction = digitalio.Direction.OUTPUT


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
base_delay = 0.25
CHAR_DELAYS = {
    ".": [base_delay, base_delay],
    "-": [3*base_delay, base_delay],
    " ": [0, 3*base_delay],
    "/": [0, 7*base_delay]
}

while True:
    user_input = input("Enter the string to translate, or type '-q' to quit. ") #prints out a space for you to type words in moniter
    user_input = user_input.upper()
    if user_input == "-Q": # uppercase because of the previous line
        break #everything stops if you type -q in
    morse_translation = ""
    translation_good = True # flag to be set if we hit an unknown character
    for letter in user_input:
        if letter == " ":
            morse_translation += "/" #if you put a space, it makes a break
        else:
            try:
                morse_translation += MORSE_CODE[letter] + " "
            except KeyError:
                print(f"Unsupported character \"{letter}\" used. Please try again.") #if you put in a letter that isn't in the above definitions, it tells you
                translation_good = False
                break #everything stop
    if translation_good:
        print(morse_translation)
        for pulse in morse_translation:
            on_delay, off_delay = CHAR_DELAYS[pulse]
            if on_delay == 0: # bypass ever turning the LED on
                time.sleep(off_delay)
            else:
                led.value = True
                time.sleep(on_delay)
                led.value = False
                time.sleep(off_delay)
            
print("Thanks for using the Morse Code Translator. Goodbye!")