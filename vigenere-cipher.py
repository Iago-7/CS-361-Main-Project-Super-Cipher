"""
A Vigenère cipher uses a key word to determine how many letters to shift a letter to be converted. For example, if the
key word is "Lemon" and the string to encrypt is "Grapefruit," the first letter to be converted ("G") will use "L" as
the key to know how many letters G is to be shifted. L's distance from A is 11, so G will shift 11 letters, and "R" will
be the first letter in the encryption. The process is repeated with the letter to be encrypted becoming "r" and the
letter from the key word to be used to shift r will be "e" (the second letter in Lemon). The process repeats, and the
key word is repeated to match the length of the string to be encrypted, so in this case LemonLemon will be used as the
key word.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = 5002


@app.route('/', methods=['POST'])
def vigenere_cipher():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Data not found, please try again."}), 400

    if "string_to_encrypt" not in data:
        return jsonify({"error": "string_to_encrypt not found, please try again."}), 400

    if "encrypt_key" not in data:
        return jsonify({"error": "encrypt_key not found, please try again."}), 400

    try:
        encrypt_string = data["string_to_encrypt"]
        key_string = data["encrypt_key"]
    except (ValueError, TypeError):
        return jsonify({"error": "incorrect data type for encrypt_string or key_string, please try again."}), 400

    letter_string_lower = "abcdefghijklmnopqrstuvwxyz"
    letter_string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_string_pos = 0
    final_string = ""
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

    return jsonify({"encrypted_string": final_string}), 200


if __name__ == "__main__":
    app.run(port=PORT)
