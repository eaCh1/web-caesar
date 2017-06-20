"""
Function for the Ceasar crypting
"""
def alphabet_position(symbol):
    '''Returns the 0-based numerical position of the given letter in the English alphabet'''
    alphabet_caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lows = "abcdefghijklmnopqrstuvwxyz"

    if symbol in alphabet_caps:
        return alphabet_caps.index(symbol)
    elif symbol in alphabet_lows:
        return alphabet_lows.index(symbol)
    else:
        return symbol

def rotate_character(char, rot):
    """Takes a character, finds its position, then shifts to the right by the integer provided"""
    alphabet_caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet_lows = "abcdefghijklmnopqrstuvwxyz"
    if char.isupper():
        first_position = alphabet_position(char)
        new_position = int(first_position + rot)
        if new_position >= 26:
            new_position = new_position % 26
        return alphabet_caps[new_position]
    elif char.islower():
        first_position = alphabet_position(char)
        new_position = int(first_position + rot)
        if new_position >= 26:
            new_position = new_position % 26
        return alphabet_lows[new_position]
    else:
        return char


def rotate_string(text, rot):
    '''function to rotate characters in a textstring by given integer'''
    wrk_lst = []
    wrk_char = ""
    for item in text:
        wrk_char = rotate_character(item, rot)
        wrk_lst.append(wrk_char)
    wrk_lst = ''.join(wrk_lst)
    return wrk_lst

def main():
    '''main  operations of the program'''

    text = str(input("Type a message:"))
    rot = int(input("Rotate by:"))

    print(rotate_string(text, rot))
if __name__ == "__main__":
    main()
