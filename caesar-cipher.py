"""
Name: Steven Wallace
Class: CS361
Project: Microservice: Cipher
Description: Get an integer from the user and shifts the letters in the cipher-data.txt that many characters. Then
return the data.
"""

import time
import os
import sys


def get_user_input():
    valid_input = False
    while not valid_input:
        user_input = input()
        try:
            user_input_int = int(user_input)
            valid_input = True
            return user_input_int
        except ValueError:
            if user_input.lower() in ["x", "exit"]:
                print("Thank you for using the Cipher. Goodbye.")
                sys.exit(0)
            else:
                print("Please type a valid integer.")


"""
Source: Shift letters by a certain value in python
URL: https://stackoverflow.com/questions/48514673/shift-letters-by-a-certain-value-in-python 
Usage: I used this as a reference to create the letter shift.
"""


def shift_letters(letter, shift):
    new_letter = ord(letter) + shift
    if 'A' <= letter <= 'Z':
        return chr((new_letter - ord('A')) % 26 + ord('A'))
    elif 'a' <= letter <= 'z':
        return chr((new_letter - ord('a')) % 26 + ord('a'))
    else:
        print("Invalid character in input. Please make sure the input is alphabetic and try again.")
        sys.exit(0)


def read_file(file_path):
    with open(file_path, "r") as original_text:
        return original_text.read()


def write_file(file_path, data):
    with open(file_path, "w") as cipher_data:
        cipher_data.write(data)


def process_cipher(file_string, cipher_num):
    string_array = list(file_string)
    for i in range(len(string_array)):
        string_array[i] = shift_letters(string_array[i], cipher_num)
    return ''.join(string_array)


def handle_user_choice():
    valid_input = False
    while not valid_input:
        user_input = input().lower()
        if user_input in ["yes", "no", "x", "exit"]:
            if user_input == "yes":
                start_cipher()
            else:
                print("Thank you for using the Cipher. Goodbye.")
                sys.exit(0)
        else:
            print("Please type a valid input.")


def start_cipher():
    time.sleep(1)
    print("\nCipher Microservice\n")
    print("The Cipher gets an integer from the user and shifts the letters read from cipher-data.txt that many times.")
    print("Input 'x' or the word 'exit' to exit the program.\n")
    print("Input an integer for the cipher:")

    cipher_num = get_user_input()

    path_dirname = os.path.dirname(__file__)
    file_path = os.path.join(path_dirname, "cipher-data.txt")
    file_string = read_file(file_path)

    cipher_result = process_cipher(file_string, cipher_num)
    print("The cipher shifted value is: " + cipher_result)

    write_file(file_path, cipher_result)
    print("The shifted value has been written to cipher-data.txt\n")
    print("Input a different number? [yes/no]")

    handle_user_choice()


# Start the Cipher
start_cipher()
