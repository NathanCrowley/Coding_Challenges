'''
function to convert string to morse code
'''

def to_morse(string):
    morse_string = ''
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    for character in string:
        character = character.upper()
        morse_string += char_to_dots[character]

    return '{} --> {}'.format(string,morse_string)

#--------------------------------------TEST-------------------------------
print(to_morse('EDABBIT CHALLENGE'))
print(to_morse('help me!'))
print(to_morse('nathan crowley'))
print(to_morse('up the ra'))
print(to_morse('TudWRgO9m9'))
print(to_morse('91NkDYN4Ir'))
print(to_morse('Tara ruane'))