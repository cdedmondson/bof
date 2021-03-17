############################################################################
# Class: Right_Module
# Purpose:
############################################################################
from BOF import BOF


class Right_Module(BOF):

    # Constructor
    def __init__(self):
        super().__init__()  # Call to superclass

    ##############################################################################
    # Method: display_first_step
    # Purpose:
    ##############################################################################
    def display_first_step(self):
        return print(self.color_text('blue', "\tLook for a DLL that has no memory protections using mona.py\n") +
                     self.color_text('green', '\t\n> Command: ') +
                     self.color_text('red', '!mona modules\n'))

    ##############################################################################
    # Method: display_second_step
    # Purpose:
    ##############################################################################
    def display_second_step(self):
        return print(self.color_text('blue',
                                     "\tLook for something attached to program we are attacking that shows false for the following memory protections:\n") +
                     self.color_text('green', '\t\n> Look for: ') +
                     self.color_text('red', 'Rebase | SafeSEH | ASLR  | NXCompat |\n'))

    ##############################################################################
    # Method: display_third_step
    # Purpose:
    ##############################################################################
    def display_third_step(self):
        return print(self.color_text('blue',
                                     "\tFind the instruction") +
                     self.color_text('magenta', ' JMP ESP ') +
                     self.color_text('blue', 'in module:\n') +
                     self.color_text('green', '\t\n> Command: ') +
                     self.color_text('red', ' !mona find -s "\\xff\\xe4" -m <module .dll>\n'))
