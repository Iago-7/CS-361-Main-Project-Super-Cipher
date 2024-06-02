"""
The opposite cipher takes a string of alphanumeric characters and converts each one to their "opposite." For example, if
you arranged each letter (or number) around the edge of a circle (like a clock), the character to be converted is
converted into the character on the opposite side of the circle. A --> N, 1 --> 6, etc.
"""

letter_string_lower = "abcdefghijklmnopqrstuvwxyz"
letter_string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_string = "0123456789"
final_string = ""

encrypt_string = input("Please enter a string to be encrypted. Non-alphanumeric characters will remain the same.\n")

for char in encrypt_string:
    if char.islower():
        pos = letter_string_lower.rfind(char)
        final_string += letter_string_lower[(pos + 13) % 26]
    elif char.isupper():
        pos = letter_string_upper.rfind(char)
        final_string += letter_string_upper[(pos + 13) % 26]
    elif char.isdigit():
        pos = numbers_string.rfind(char)
        final_string += numbers_string[(pos + 5) % 10]
    else:
        final_string += char

print(final_string)
