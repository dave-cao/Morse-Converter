# You have a string, you want to convert that into morse code

# Figure out how to convert string into morse code

DIT = "*"
DAH = "_"
MORSE_CODE_MAP = {
    "A": "*_",
    "B": "_***",
    "C": "_*_*",
    "D": "_**",
    "E": "*",
    "F": "**_*",
    "G": "__*",
    "H": "****",
    "I": "**",
    "J": "*___",
    "K": "_*_",
    "L": "*_**",
    "M": "__",
    "N": "_*",
    "O": "___",
    "P": "*__*",
    "Q": "__*_",
    "R": "*_*",
    "S": "***",
    "T": "_",
    "U": "**_",
    "V": "***_",
    "W": "*__",
    "X": "_**_",
    "Y": "_*__",
    "Z": "__**",
    "1": "*____",
    "2": "**___",
    "3": "***__",
    "4": "****_",
    "5": "*****",
    "6": "_****",
    "7": "__***",
    "8": "___**",
    "9": "____*",
    "0": "_____",
    " ": "",
}


def to_morse(string):
    morsed_string = [
        MORSE_CODE_MAP[letter] for letter in string.upper() if letter in MORSE_CODE_MAP
    ]
    morsed_string = " ".join(morsed_string)
    return morsed_string


morsed_string = to_morse("Hello world")


def from_morse(string):
    split = string.split(" ")

    from_morse_string = [
        key for code in split for key, value in MORSE_CODE_MAP.items() if code == value
    ]
    readable_string = "".join(from_morse_string).lower()
    print(readable_string)


from_morse(morsed_string)
