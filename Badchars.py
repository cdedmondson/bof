############################################################################
# Class: Badchars
# Purpose:
############################################################################
from BOF import BOF
import sys


class Badchars(BOF):

    # Constructor
    def __init__(self):
        super().__init__()  # Call to superclass

    ##############################################################################
    # Method: first_step
    # Purpose:
    ##############################################################################
    def first_step(self):
        return print(self.color_text('blue',
                                     "\tStep 1: Send all possible 255 characters in hex and look for abnormal characters\n") +
                     self.color_text('magenta', '\n\tBad Characters 1-255\n'))

    ##############################################################################
    # Method: generate_bad_characters
    # Purpose:
    ##############################################################################
    def generate_bad_characters(self, offset):
        counter = 0
        print("badchars=(")
        for chars in range(1, 256):  # Write each HEX character 1-256 skipping NULL byte
            if counter == 0:
                print('"', end="")
            elif counter % 16 == 0:  # Every 16 characters add quotation mark to front of line
                print('"', end="")
            sys.stdout.write("\\x" + '{:02x}'.format(chars))  # Append \x to every HEX character
            if chars % 16 == 0:  # Every 16 characters add quotation mark to end of line
                print('"')
            counter = counter + 1

        print('"', end="" + ")" + "\n\n")

        return print(self.color_text('red', f"\tpayload = 'A' * {offset} + 'B' * 4 + badchars" + "\n"))

    ##############################################################################
    # Method: get_badchars_from_user
    # Purpose:
    ##############################################################################
    def get_badchars_from_user(self):
        return self.user_input('blue', '[+] Enter bad characters')
