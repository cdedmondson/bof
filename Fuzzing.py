############################################################################
# Class: Fuzzing
# Purpose: Encapsulate fuzzing procedures and methods
############################################################################

# Import BOF class for inheritance
from BOF import BOF


# Begin class
class Fuzzing(BOF):

    # Constructor
    def __init__(self, byte_count):
        self.__byte_count = byte_count
        super().__init__()  # Call to superclass

    ##############################################################################
    # Method: first_step
    # Purpose: Return 1st instructions for fuzzing
    ##############################################################################
    def first_step(self):
        return print(self.color_text('blue', "\tStep 1: Send ") +
                     self.color_text('red', '100') +
                     self.color_text('blue', " bytes at a time"))

    ##############################################################################
    # Method: second_step
    # Purpose: Return 2nd instructions for fuzzing
    ##############################################################################
    def second_step(self):
        return print(self.color_text('magenta', "\tStep 2: Wait for crash and note byte count"))

    ##############################################################################
    # Method: get_byte_count
    # Purpose: Return byte count
    ##############################################################################
    def get_byte_count(self):
        return self.__byte_count

    ##############################################################################
    # Method: user_input
    # Purpose: Receive byte count. If input is not an integer continue to prompt
    #          user until input is correct.
    ##############################################################################
    def user_input(self, color, message):
        while True:
            try:
                self.__byte_count = int(BOF.user_input(self, color, message))
                return
            except ValueError:
                print(BOF.color_text(self, 'bred', "\n[!] Please enter a number."))
                continue
