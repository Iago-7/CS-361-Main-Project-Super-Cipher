"""
The opposite cipher takes a string of alphanumeric characters and converts each one to their "opposite." For example, if
you arranged each letter (or number) around the edge of a circle (like a clock), the character to be converted is
converted into the character on the opposite side of the circle. A --> N, 1 --> 6, etc.
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

PORT = 5000


@app.route('/', methods=['POST'])
def opposite_cipher():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Data not found, please try again."}), 400

    if "string_to_encrypt" not in data:
        return jsonify({"error": "string_to_encrypt not found, please try again."}), 400

    try:
        encrypt_string = data["string_to_encrypt"]
    except (ValueError, TypeError):
        return jsonify({"error": "incorrect data type for string_to_encrypt, please try again."}), 400

    letter_string_lower = "abcdefghijklmnopqrstuvwxyz"
    letter_string_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_string = "0123456789"
    final_string = ""

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

    return jsonify({"encrypted_string": final_string}), 200


if __name__ == "__main__":
    app.run(port=PORT)
