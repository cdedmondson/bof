############################################################################
# Class: Offset
# Purpose: Encapsulate all processes needed to overwrite the EIP
############################################################################
from BOF import BOF


class Overwriting_EIP(BOF):

    # Constructor
    def __init__(self):
        super().__init__()  # Call to superclass

    ##############################################################################
    # Method: display_first_step
    # Purpose:
    ##############################################################################
    def display_first_step(self):
        return print(self.color_text('blue', "\tStep 1.  Once we have the offset send ") +
                     self.color_text('red', "'A's") +
                     self.color_text('blue', " the same size as offset, then four") +
                     self.color_text('red', " 'B's") +
                     self.color_text('blue', ".  The EIP should be overwritten with") +
                     self.color_text('red', " '42424242'") +
                     self.color_text('blue', " (if not redo step 2)"))

    ##############################################################################
    # Method: show_payload
    # Purpose:
    ##############################################################################
    def show_payload(self, offset):
        return print(self.color_text('magenta', f"\n\tpayload = 'A' * {offset} + 'B' * 4"))
