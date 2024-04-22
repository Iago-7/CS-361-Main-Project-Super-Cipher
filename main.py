from random import choice

LOGO_1 = "   _____                          _______       __\n"
LOGO_2 = "  / ___/__  ______  ___  _____   / ____(_)___  / /_  ___  _____\n"
LOGO_3 = "  \\__ \\/ / / / __ \\/ _ \\/ ___/  / /   / / __ \\/ __ \\/ _ \\/ ___/\n"
LOGO_4 = " ___/ / /_/ / /_/ /  __/ /     / /___/ / /_/ / / / /  __/ /\n"
LOGO_5 = "/____/\\__,_/ .___/\\___/_/      \\____/_/ .___/_/ /_/\\___/_/\n"
LOGO_6 = "        /_/                        /_/"
LOGO = LOGO_1 + LOGO_2 + LOGO_3 + LOGO_4 + LOGO_5 + LOGO_6
USER_CHOICE_MESSAGE = ("please type the number corresponding to the option you'd like, and hit enter:\n"
                       "0 - What is Super Cipher?\n"
                       "1 - See our latest features.\n"
                       "2 - See an explanation about what a cipher is.\n"
                       "3 - Encrypt a message with a Caesar cipher.\n"
                       "4 - Encrypt a message with a Mirror cipher.\n"
                       "5 - Encrypt a message with a Vigenère cipher.\n"
                       "6 - Encrypt a message with a Date-shift cipher.\n"
                       "7 - Exit.\n")
WHAT_IS_SUPER_CIPHER = ("Super Cipher allows users to encrypt a message of up to 1,000 characters in length by one of "
                        "four different methods, or ciphers.")
LATEST_FEATURES_TEXT = ("we now currently have all four cipher types available! Please enjoy! Also, be on the lookout "
                        "for Super Decipher coming next year!")
WHAT_IS_A_CIPHER_TEXT = ("a cipher is a secret or coded way of writing. Different ciphers encrypt, or scramble text "
                         "differently, and readers of a ciphered text need a specific key to decrypt the text into a "
                         "readable form.")
NICKNAME_LIST = ["Knuckle", "Scapula", "Tibia", "Femur", "Radius", "Ulna", "Skull", "Pelvis", "Thumb", "Humerus"]

print("Hello fellow cryptologist! Welcome to...")
print(LOGO)

is_user_name_unconfirmed = True
while is_user_name_unconfirmed:
    # TODO: ADD ERROR CHECKING FOR ENTRY
    user_name = input("First, please type your first name and hit enter. Don't worry! We'll keep your name private! "
                      "Otherwise, type 'nickname' and we'll give you an alias to go by. ")
    if user_name == "nickname":
        user_name = choice(NICKNAME_LIST)
        print(f"You have been given the alias {user_name}!")
    name_confirmation = int(input(f"Next, please type 1 followed by enter if {user_name} is the name you'd like to go "
                                  f"by, otherwise, type 0 followed by enter if you'd like to enter your name again or "
                                  f"receive a different alias. "))
    # TODO: ADD ERROR CHECKING FOR ENTRY
    if name_confirmation == 1:
        is_user_name_unconfirmed = False

print(f"Glad to have you aboard {user_name}! Let's get started on the next step!")

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
        pass  # TODO: load Caesar cipher
    elif user_choice == 4:
        pass  # TODO: load Mirror cipher
    elif user_choice == 5:
        pass  # TODO: load Vigenère cipher
    elif user_choice == 6:
        pass  # TODO: load Date-shift cipher
    elif user_choice == 7:
        print(f"Thanks for stopping by {user_name}! We'll see you next time!")
        break
    user_choice = int(input(f"{user_name}, {USER_CHOICE_MESSAGE}"))
