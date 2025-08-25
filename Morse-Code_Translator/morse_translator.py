# Morse code dictionary:
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

REVERSE_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

def encode_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char == ' ':
            morse_code.append(' ')  # Separate words by space
        elif char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
        else:
            morse_code.append('?')  # Unknown characters
    return ' '.join(morse_code)

def decode_from_morse(morse):
    words = morse.split('   ')  # Morse words separated by 3 spaces
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_letters = []
        for letter in letters:
            decoded_letters.append(REVERSE_MORSE_CODE_DICT.get(letter, '?'))
        decoded_words.append(''.join(decoded_letters))
    return ' '.join(decoded_words)

print("Morse Code Translator")
choice = input("Type 'E' to encode text to Morse or 'D' to decode Morse to text: ").strip().upper()

if choice == 'E':
    text = input("Enter the text to encode: ")
    encoded = encode_to_morse(text)
    print(f"Encoded Morse:\n{encoded}")

elif choice == 'D':
    print("Note: Separate Morse letters with spaces and words with 3 spaces.")
    morse = input("Enter the Morse code to decode: ")
    decoded = decode_from_morse(morse)
    print(f"Decoded Text:\n{decoded}")

else:
    print("Invalid choice. Please run the program again and type 'E' or 'D'.")