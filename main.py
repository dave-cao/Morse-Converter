"""
This program converts a user inputted string or a text file into morse code.
It also converts from morse code back into readable English.

Some caveats:
    1. When going back into English, the resulting text will all be lowercase
    2. If a non morse file contains morse like characters like **, that will be converted into morse code.
"""
import sys

from variables import MORSE_CODE_MAP


def main():

    if len(sys.argv) == 1:
        # If only one argument is given, then ask for a string
        user_choice = input("[1] English to Morse Code\n[2] Morse Code to English\n\n")
        user_string = input("Alright, give me your string:\n")

        if user_choice == "1":
            print(to_morse(user_string))
        elif user_choice == "2":
            print(from_morse(user_string))

    elif len(sys.argv) == 2:
        # If an argument is given, then convert the file into morse
        try:
            with open(sys.argv[1], "r") as file:
                data = file.read()
        except FileNotFoundError:
            print("Please provide a valid file to convert!")
            return

        print("Please choose one of the options...")
        user_choice = input("[1] English to Morse Code\n[2] Morse Code to English\n\n")

        if user_choice == "1":
            with open(f"morse_{sys.argv[1]}", "w") as file:
                file.write(to_morse(data))
        elif user_choice == "2":
            with open(f"english_{sys.argv[1]}", "w") as file:
                file.write(from_morse(data))
        else:
            print("Not a valid option.")

    else:
        print("I only take one argument! Sorry, try again!")


def to_morse(string):
    """Converts a string into it's morse code equivalent.
    Args:
        string(str): the string to convert into morse
    Returns:
        morsed_string(str): the resulting morse code
    """
    morsed_string = [
        MORSE_CODE_MAP[letter] if letter in MORSE_CODE_MAP else letter
        for letter in string.upper()
    ]
    morsed_string = " ".join(morsed_string)
    return morsed_string


def from_morse(string):
    """Takes a morse string and converts it back into readable english
    Args:
        string(str): the string to convert into english
    Returns:
        readable_string(str): the english version of the morse code
    """

    split = string.split(" ")

    from_morse_string = []
    for code in split:
        count = 0
        for key, value in MORSE_CODE_MAP.items():
            if code == value:
                from_morse_string.append(key)
            else:
                count += 1

            # If we reached the end without seeing a morse, then just use the original
            # character
            if count == len(MORSE_CODE_MAP):
                from_morse_string.append(code)

    readable_string = "".join(from_morse_string).lower()
    return readable_string


main()
