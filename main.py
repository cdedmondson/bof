############################################################################
# Author: Cameron Edmondson
# Purpose: Walk students through buffer overflow process step by step
#          with visuals and tips displayed in Kali Linux terminal.
# Version 1.0
# Date Last Modified: 11/11/2020
############################################################################
from BOF import BOF
from Badchars import Badchars
from Fuzzing import Fuzzing
from Offset import Offset
from Overwriting_EIP import Overwriting_EIP
from Right_Module import Right_Module
from Generate_ShellCode import Generate_ShellCode


def main():
    bof = BOF()
    fuz = Fuzzing(0)
    eip = Overwriting_EIP()
    badchars = Badchars()
    rm = Right_Module()
    gs = Generate_ShellCode()

    bof.steps_to_conduct_bof()  # Display BOF steps in terminal

    bof.display_current_step("1. Fuzzing")  # Display current step

    fuz.first_step()  # Display first sub step
    fuz.second_step()  # Display second sub step

    fuz.user_input('blue', '[+] Enter byte count at which program crashed')

    bof.display_current_step("\n2. Finding the Offset")

    offset = Offset(fuz.get_byte_count())

    offset.display_first_step()

    offset.pattern_create()

    offset.display_unique_bytes()

    offset.display_second_step()

    offset_result = offset.get_offset()  # Stored returned offset value

    offset.display_offset(offset_result)  # Display

    bof.display_current_step("\n3. Overwriting EIP")

    eip.display_first_step()

    eip.show_payload(offset_result)

    bof.display_current_step("\n4. Finding Bad Characters")

    badchars.first_step()

    badchars.generate_bad_characters(offset_result)

    bc = badchars.get_badchars_from_user()

    bof.display_current_step("\n5. Finding the Right Module")

    rm.display_first_step()

    rm.display_second_step()

    rm.display_third_step()

    bof.display_current_step("\n6. Generating Shellcode")

    lhost_ip = gs.user_input('blue', "[+] Enter Local Host's IP address ")

    lport = gs.user_input('blue', "[+] Enter Local Port address ")

    gs.generateShellCode(lhost_ip, int(lport), str(bc))


if __name__ == '__main__':
    main()
