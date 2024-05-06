from random import choice

LOGO_1 = "   _____                          _______       __\n"
LOGO_2 = "  / ___/__  ______  ___  _____   / ____(_)___  / /_  ___  _____\n"
LOGO_3 = "  \\__ \\/ / / / __ \\/ _ \\/ ___/  / /   / / __ \\/ __ \\/ _ \\/ ___/\n"
LOGO_4 = " ___/ / /_/ / /_/ /  __/ /     / /___/ / /_/ / / / /  __/ /\n"
LOGO_5 = "/____/\\__,_/ .___/\\___/_/      \\____/_/ .___/_/ /_/\\___/_/\n"
LOGO_6 = "          /_/                      /_/"
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
    is_user_name_unconfirmed = True
    while is_user_name_unconfirmed:
        # TODO: ADD ERROR CHECKING FOR ENTRY
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
        # TODO: ADD ERROR CHECKING FOR ENTRY
        if name_confirmation == 1:
            is_user_name_unconfirmed = False
    return name


def main_menu():
    # TODO: ADD TRY/CATCH HERE FOR NON-NUMERICAL INPUT
    user_choice = int(input(f"{user_name}, {USER_CHOICE_MESSAGE}"))
    while True:
        if user_choice == 0:
            print(f"Great question {user_name}! {WHAT_IS_SUPER_CIPHER}")
        elif user_choice == 1:
            print(f"Thanks for inquiring {user_name}, {LATEST_FEATURES_TEXT}")
        elif user_choice == 2:
            print(f"{user_name}, {WHAT_IS_A_CIPHER_TEXT}")
        elif user_choice == 3:
            txt_to_encrypt = input(f"{user_name}, please type up to 1,000 characters of text to be encrypted. WARNING:"
                                   f" once you hit enter, you will not be able to change your text.\n")
            return txt_to_encrypt
        elif user_choice == 4:
            return False
        user_choice = int(input(f"{user_name}, {USER_CHOICE_MESSAGE}"))


def encryption_menu():
    while True:
        cipher_choice = int(input(f"{user_name}, please choose from the following options:\n"
                                  f"0 - Caesar cipher\n"
                                  f"1 - Mirror cipher\n"
                                  f"2 - Vigenère cipher\n"
                                  f"3 - Date-shift cipher\n"))
        if cipher_choice == 0:
            # TODO: encrypt text with Caesar cipher.
            return "Encrypted Text"
        if cipher_choice == 1:
            # TODO: encrypt text with Mirror cipher.
            return "Encrypted Text"
        if cipher_choice == 2:
            # TODO: encrypt text with Vigenère cipher.
            return "Encrypted Text"
        if cipher_choice == 3:
            # TODO: encrypt text with Date-shift cipher.
            return "Encrypted Text"


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
        print(f"{user_name}, here is your encrypted text: {encrypted_text}\n")
    continue_or_exit_choice = int(input(f"{user_name}, type 1 and hit enter to return to the main menu, or type 2 and "
                                        f"hit enter to exit.\n"))
    if continue_or_exit_choice == 2:
        break

print(f"Thanks for stopping by {user_name}! We'll see you next time!")
