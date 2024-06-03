"""
A date-shift cipher uses a date as a key to determine how many letters to shift a letter to be converted. For example,
if the date entered is "01/31/1985" and the string to be converted is "Bananas are great," the key becomes 01311985. The
"B" in bananas is shifted 0 places and remains "B," the "a" shifts 1 place and becomes "b," the "n" shifts 3 places and
becomes "q," etc. The key is repeated to match the number of letters in the string to be encrypted, so in this case the
key would become 013119850131198 to match the 15 characters being converted in "Bananas are great."
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = 5001


@app.route('/', methods=['POST'])
def date_shift_cipher():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Data not found, please try again."}), 400

    if "string_to_encrypt" not in data:
        return jsonify({"error": "string_to_encrypt not found, please try again."}), 400

    if "encrypt_key" not in data:
        return jsonify({"error": "encrypt_key not found, please try again."}), 400

    try:
        encrypt_string = data["string_to_encrypt"]
        date_input = data["encrypt_key"]
    except (ValueError, TypeError):
        return jsonify({"error": "incorrect data type for time_in_minutes, please try again."}), 400

    letter_string_lower = "abcdefghijklmnopqrstuvwxyz"
    letter_string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_string_pos = 0
    final_string = ""
    key_string = ""

    for char in date_input:
        if char.isdigit():
            key_string += char

    for letter in encrypt_string:
        if letter.islower():
            current_letter_pos = letter_string_lower.rfind(letter)
            shift_amount = int(key_string[key_string_pos])
            key_string_pos = (key_string_pos + 1) % len(key_string)
            final_string += letter_string_lower[(current_letter_pos + shift_amount) % 26]
        elif letter.isupper():
            current_letter_pos = letter_string_upper.rfind(letter)
            shift_amount = int(key_string[key_string_pos])
            key_string_pos = (key_string_pos + 1) % len(key_string)
            final_string += letter_string_upper[(current_letter_pos + shift_amount) % 26]
        else:
            final_string += letter

    return jsonify({"encrypted_string": final_string}), 200


if __name__ == "__main__":
    app.run(port=PORT)
