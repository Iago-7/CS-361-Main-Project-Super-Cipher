"""
A Vigenère cipher uses a key word to determine how many letters to shift a letter to be converted. For example, if the
key word is "Lemon" and the string to encrypt is "Grapefruit," the first letter to be converted ("G") will use "L" as
the key to know how many letters G is to be shifted. L's distance from A is 11, so G will shift 11 letters, and "R" will
be the first letter in the encryption. The process is repeated with the letter to be encrypted becoming "r" and the
letter from the key word to be used to shift r will be "e" (the second letter in Lemon). The process repeats, and the
key word is repeated to match the length of the string to be encrypted, so in this case LemonLemon will be used as the
key word.
"""

letter_string_lower = "abcdefghijklmnopqrstuvwxyz"
letter_string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key_string_pos = 0
final_string = ""

encrypt_string = input("Please enter a string to be encrypted. Non-alphabet characters will will remain the same.\n")
key_string = input("Please enter a word to use as a key. Letters only.\n")
key_string = key_string.lower()

for char in encrypt_string:
    if char.islower():
        current_letter_pos = letter_string_lower.rfind(char)
        shift_amount = (letter_string_lower.rfind(key_string[key_string_pos]) + current_letter_pos)
        key_string_pos = (key_string_pos + 1) % len(key_string)
        final_string += letter_string_lower[shift_amount % 26]
    elif char.isupper():
        current_letter_pos = letter_string_upper.rfind(char)
        shift_amount = (letter_string_lower.rfind(key_string[key_string_pos]) + current_letter_pos)
        key_string_pos = (key_string_pos + 1) % len(key_string)
        final_string += letter_string_upper[shift_amount % 26]
    else:
        final_string += char

print(final_string)
