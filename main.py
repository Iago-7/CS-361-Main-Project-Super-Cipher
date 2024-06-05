from random import choice
import requests
import json
import os
import subprocess

LOGO_1 = "   _____                          _______       __\n"
LOGO_2 = "  / ___/__  ______  ___  _____   / ____(_)___  / /_  ___  _____\n"
LOGO_3 = "  \\__ \\/ / / / __ \\/ _ \\/ ___/  / /   / / __ \\/ __ \\/ _ \\/ ___/\n"
LOGO_4 = " ___/ / /_/ / /_/ /  __/ /     / /___/ / /_/ / / / /  __/ /\n"
LOGO_5 = "/____/\\__,_/ .___/\\___/_/      \\____/_/ .___/_/ /_/\\___/_/\n"
LOGO_6 = "          /_/                        /_/"
LOGO = LOGO_1 + LOGO_2 + LOGO_3 + LOGO_4 + LOGO_5 + LOGO_6
USER_CHOICE_MESSAGE = ("please type the number corresponding to the option you'd like, and hit enter:\n"
                       "0 - What is Super Cipher?\n"
                       "1 - See our latest features.\n"
                       "2 - See an explanation about what a cipher is.\n"
                       "3 - Enter text to be encrypted.\n"
                       "4 - Exit.\n")
WHAT_IS_SUPER_CIPHER = ("Super Cipher allows users to encrypt a message of up to 1,000 characters in length by one of "
                        "four different methods, or ciphers.\n")
LATEST_FEATURES_TEXT = ("we now currently have all four cipher types available! Please enjoy! Also, be on the lookout "
                        "for Super Decipher coming next year!\n")
WHAT_IS_A_CIPHER_TEXT = ("a cipher is a secret or coded way of writing. Different ciphers encrypt, or scramble, text "
                         "differently, and readers of a ciphered text need a specific key to decrypt the text into a "
                         "readable form.\n")
NICKNAME_LIST = ["Knuckle", "Scapula", "Tibia", "Femur", "Radius", "Ulna", "Skull", "Pelvis", "Thumb", "Humerus"]


def get_user_name():
    name = ""
    is_user_name_unconfirmed = True
    while is_user_name_unconfirmed:
        name = input(
            "First, please type your first name and hit enter. Don't worry! We'll keep your name private! "
            "Otherwise, type 'nickname' and we'll give you an alias to go by.\n")
        if name == "nickname":
            name = choice(NICKNAME_LIST)
            print(f"You have been given the alias {name}!")
        name_confirmation = int(
            input(f"Next, please type 1 followed by enter if {name} is the name you'd like to go "
                  f"by, otherwise, type 2 followed by enter if you'd like to enter your name again or "
                  f"receive a different alias.\n"))
        if name_confirmation == 1:
            is_user_name_unconfirmed = False
    return name


def main_menu():
    valid_entry = False
    user_choice = None
    while valid_entry is False:
        try:
            user_choice = int(input(f"{user_name}, {USER_CHOICE_MESSAGE}"))
            valid_entry = True
        except (ValueError, TypeError):
            print("Incorrect input, please enter a number between 0 and 4.\n")
    while True:
        if user_choice == 0:
            print(f"Great question {user_name}! {WHAT_IS_SUPER_CIPHER}")
        elif user_choice == 1:
            print(f"Thanks for inquiring {user_name}, {LATEST_FEATURES_TEXT}")
        elif user_choice == 2:
            print(f"{user_name}, {WHAT_IS_A_CIPHER_TEXT}")
        elif user_choice == 3:
            ready_to_encrypt = True
            return ready_to_encrypt
        elif user_choice == 4:
            return False
        user_choice = int(input(f"{user_name}, {USER_CHOICE_MESSAGE}"))


def encryption_menu():
    while True:
        valid_entry = False
        cipher_choice = None
        while valid_entry is False:
            try:
                cipher_choice = int(input(f"{user_name}, please choose from the following options:\n"
                                          f"0 - Caesar cipher\n"
                                          f"1 - Opposite cipher\n"
                                          f"2 - Vigenère cipher\n"
                                          f"3 - Date-shift cipher\n"))
                valid_entry = True
            except (ValueError, TypeError):
                print("Incorrect input, please enter a number between 0 and 3.\n")
        if cipher_choice == 0:
            path_directory_name = os.path.dirname(__file__)
            file_path = os.path.join(path_directory_name, "cipher-data.txt")
            data = input(f"{user_name}, please type up to 1,000 characters of text to be encrypted. Alphanumeric "
                         f"characters ONLY, and NO whitespace. WARNING: once you hit enter, you will not be able to "
                         f"change your text.\n")
            with open(file_path, "w") as cipher_data:
                cipher_data.write(data)

            subprocess.run(["python3", "caesar-cipher.py"])
            return None
        if cipher_choice == 1:
            opposite_url = "http://127.0.0.1:5000"
            encrypt_string = input(f"{user_name}, please type up to 1,000 characters of text to be encrypted. "
                                   f"Non-alphanumeric characters will remain the same. WARNING:"
                                   f" once you hit enter, you will not be able to change your text.\n")
            cipher_data = {"string_to_encrypt": encrypt_string}
            json_data = json.dumps(cipher_data)
            headers = {"Content-Type": "application/json"}
            response = requests.post(opposite_url, data=json_data, headers=headers)
            json_response = response.json()
            opposite_encrypted_text = json_response["encrypted_string"]
            return opposite_encrypted_text
        if cipher_choice == 2:
            vigenere_url = "http://127.0.0.1:5002"
            encrypt_string = input(f"{user_name}, please type up to 1,000 characters of text to be encrypted. "
                                   f"Non-letter characters will will remain the same. WARNING:"
                                   f" once you hit enter, you will not be able to change your text.\n")
            key_input = input("Please enter a word to use as a key. Letters only. WARNING: once you hit enter, you will"
                              " not be able to change your text.\n")
            cipher_data = {"string_to_encrypt": encrypt_string,
                           "encrypt_key": key_input}
            json_data = json.dumps(cipher_data)
            headers = {"Content-Type": "application/json"}
            response = requests.post(vigenere_url, data=json_data, headers=headers)
            json_response = response.json()
            vigenere_encrypted_text = json_response["encrypted_string"]
            return vigenere_encrypted_text
        if cipher_choice == 3:
            date_shift_url = "http://127.0.0.1:5001"
            encrypt_string = input(f"{user_name}, please type up to 1,000 characters of text to be encrypted. "
                                   f"Non-letter characters will will remain the same. WARNING:"
                                   f" once you hit enter, you will not be able to change your text.\n")
            date_input = input("Please enter a date in the form MM/DD/YYYY. WARNING: once you hit enter, you will not "
                               "be able to change your text.\n")
            cipher_data = {"string_to_encrypt": encrypt_string,
                           "encrypt_key": date_input}
            json_data = json.dumps(cipher_data)
            headers = {"Content-Type": "application/json"}
            response = requests.post(date_shift_url, data=json_data, headers=headers)
            json_response = response.json()
            date_shift_encrypted_text = json_response["encrypted_string"]
            return date_shift_encrypted_text


print("Hello fellow cryptologist! Welcome to...\n")
print(LOGO + "\n")

user_name = get_user_name()
print(f"Glad to have you aboard {user_name}! Let's get started on the next step!\n")

while True:
    text_to_encrypt = main_menu()
    if text_to_encrypt is False:
        break
    else:
        encrypted_text = encryption_menu()
        if encrypted_text is not None:
            print(f"{user_name}, here is your encrypted text: {encrypted_text}\n")
    continue_or_exit_choice = int(input(f"{user_name}, type 1 and hit enter to return to the main menu, or type 2 and "
                                        f"hit enter to exit.\n"))
    if continue_or_exit_choice == 2:
        break

print(f"Thanks for stopping by {user_name}! We'll see you next time!")
