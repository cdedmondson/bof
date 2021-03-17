############################################################################
# Class: BOF
# Purpose: Encapsulate procedures and methods used across all sub classes
############################################################################
import subprocess
import textwrap
from colorama import Fore, Style


# Begin class
class BOF:

    # Constructor
    def __init__(self):
        pass

    ##############################################################################
    # Method: color_text
    # Purpose: Takes in two parameters "color" and "text". Looks up corresponding
    #          color passed by user as key value pair then returns colored text
    ##############################################################################
    def color_text(self, color, text):
        color_values = {
            'bgreen': Fore.GREEN + Style.BRIGHT,
            'bred': Fore.RED + Style.BRIGHT,
            'bblue': Fore.BLUE + Style.BRIGHT,
            'byellow': Fore.YELLOW + Style.BRIGHT,
            'bmagenta': Fore.MAGENTA + Style.BRIGHT,

            'green': Fore.GREEN,
            'red': Fore.RED,
            'blue': Fore.BLUE,
            'yellow': Fore.YELLOW,
            'magenta': Fore.MAGENTA,

            'rst': Fore.RESET,
        }

        return color_values[color] + text + color_values['rst']

    ##############################################################################
    # Method: text_wrap
    # Purpose: Convert block of text into neatly presentable text block
    ##############################################################################
    def text_wrap(self, text):
        return textwrap.dedent(text)

    ##############################################################################
    # Method: display_text
    # Purpose: Display neatly formatted colored text to user
    ##############################################################################
    def display_wrapped_text(self, color, text):
        return print(self.color_text(color, self.wrap_text_block(text)))

    ##############################################################################
    # Method: convert_text_block
    # Purpose: Wrap text block neatly
    ##############################################################################
    def wrap_text_block(self, text):
        return self.text_wrap(text)

    ##############################################################################
    # Method: color_string
    # Purpose: Color a single string
    ##############################################################################
    def color_string(self, color, string):
        return self.color_text(color, string)

    ##############################################################################
    # Method: user_input
    # Purpose: Return user input from terminal
    ##############################################################################
    def user_input(self, color, message):
        print("\n" + self.message(color, message))
        return input(self.color_text('green', "--> "))

    ##############################################################################
    # Method: message
    # Purpose: Return message in color of choice
    ##############################################################################
    def message(self, color, message):
        return self.color_text(color, message)

    ##############################################################################
    # Method: steps_to_conduct_bof
    # Purpose: Display steps to conduct BOF on terminal
    ##############################################################################
    def steps_to_conduct_bof(self):
        return print(self.text_wrap(
            '''
             Steps to Conduct Buffer Overflow
    
                1.   Fuzzing
                2.   Finding the Offset
                3.   Overwriting the EIP
                4.   Finding Bad Characters
                5.   Finding the Right Module
                6.   Generating Shellcode
                7.   Root! 
            '''
        ))

    ##############################################################################
    # Method: display_current_step
    # Purpose: Display current step in BOF process
    ##############################################################################
    def display_current_step(self, current_step):
        return print(self.color_text('yellow', current_step) + "\n")

    ##############################################################################
    # Method: run_cmd
    # Purpose: Run shell command using subprocess
    ##############################################################################
    def run_cmd(self, cmd):
        return subprocess.run(cmd, shell=True)
