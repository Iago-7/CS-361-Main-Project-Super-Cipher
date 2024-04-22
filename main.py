LOGO_1 = "   _____                          _______       __\n"
LOGO_2 = "  / ___/__  ______  ___  _____   / ____(_)___  / /_  ___  _____\n"
LOGO_3 = "  \\__ \\/ / / / __ \\/ _ \\/ ___/  / /   / / __ \\/ __ \\/ _ \\/ ___/\n"
LOGO_4 = " ___/ / /_/ / /_/ /  __/ /     / /___/ / /_/ / / / /  __/ /\n"
LOGO_5 = "/____/\\__,_/ .___/\\___/_/      \\____/_/ .___/_/ /_/\\___/_/\n"
LOGO_6 = "        /_/                        /_/"
LOGO = LOGO_1 + LOGO_2 + LOGO_3 + LOGO_4 + LOGO_5 + LOGO_6

print("Hello fellow cryptologist! Welcome to...")
print(LOGO)
user_name = input("Please type your first name and hit enter. ")
print(f"Glad to have you aboard {user_name}! Let's get started!")

# ADD TRY/CATCH HERE FOR NON-NUMERICAL INPUT
user_choice = int(input(f"{user_name}, please type the number corresponding to the option you'd like, and hit enter:\n"
                        "0 - See our latest features\n"
                        "1 - Encrypt a message with a Caesar Cipher\n"
                        "2 - Encrypt a message with a Mirror Cipher\n"
                        "3 - Encrypt a message with a Vigenère Cipher\n"
                        "4 - Encrypt a message with a Date-shift Cipher\n"
                        "5 - Exit\n"))

while user_choice > 5 or user_choice < -1:
    user_choice = int(
        input(f"{user_name}, please type the number corresponding to the option you'd like, and hit enter:\n"
              "0 - See our latest features\n"
              "1 - Encrypt a message with a Caesar Cipher\n"
              "2 - Encrypt a message with a Mirror Cipher\n"
              "3 - Encrypt a message with a Vigenère Cipher\n"
              "4 - Encrypt a message with a Date-shift Cipher\n"
              "5 - Exit\n"))
if user_choice == 0:
    pass  # load latest features info
elif user_choice == 1:
    pass  # load Caesar Cipher
elif user_choice == 2:
    pass  # load Mirror Cipher
elif user_choice == 3:
    pass  # load Vigenère Cipher
elif user_choice == 4:
    pass  # load Date-shift Cipher
elif user_choice == 5:
    print(f"Thanks for stopping by {name}! We'll see you next time!")
