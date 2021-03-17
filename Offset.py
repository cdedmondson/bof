############################################################################
# Class: Offset
# Purpose: Encapsulate all offset procedures and methods
############################################################################
from BOF import BOF


class Offset(BOF):

    # Constructor
    def __init__(self, byte_count):
        self.byte_count = byte_count
        super().__init__()  # Call to superclass

    ##############################################################################
    # Method: display_first_step
    # Purpose: Display first sub step in find offset process
    ##############################################################################
    def display_first_step(self):
        colored_count = BOF.color_text(self, 'red', str(self.byte_count))
        return print(BOF.color_text(self, 'blue',
                                    f"\tStep 1: Generate unique characters with crash length {colored_count} "
                                    + BOF.color_text(self, 'blue', "found in Fuzzing phase\n\n")))

    ##############################################################################
    # Method: display_second_step
    # Purpose:
    ##############################################################################
    def display_second_step(self):
        return print(
            BOF.color_text(self, 'blue', "\tStep 2: Send unique characters and copy bytes in EIP register\n\n"))

    ##############################################################################
    # Method: display_offset
    # Purpose:
    ##############################################################################
    def display_offset(self, offset):
        return print(BOF.color_text(self, 'red', "\tOffset found at: " + BOF.color_text(self, 'green', offset)))

    ##############################################################################
    # Method: pattern_create
    # Purpose: Use metasploits pattern_create module to create unique byte pattern
    #          and output to tmp.txt file for further processing
    ##############################################################################
    def pattern_create(self):
        return BOF.run_cmd(self,
                           f"/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l {self.byte_count} > tmp.txt")

    ##############################################################################
    # Method: locate_beginning_of_file
    # Purpose: Use seek function to locate the beginning of file
    ##############################################################################
    def locate_beginning_of_file(self, file):
        return file.seek(0, 0)

    ##############################################################################
    # Method: file_buffer
    # Purpose: Read file into buffer then return to caller
    ##############################################################################
    def file_buffer(self, file):
        return file.read()

    ##############################################################################
    # Method: append_to_beginning_of_file
    # Purpose: Takes a file to write to and buffer of file previously stored
    #          then appends " payload=(' " to beginning of buffer and writes
    #          results to file
    ##############################################################################
    def append_to_beginning_of_file(self, file, data_buffer):
        return file.write("payload=('".encode() + data_buffer)  # Write unique_bytes=(' to beginning of file

    ##############################################################################
    # Method: locate_last_line_of_file
    # Purpose: Use seek function to locate end of file then return to caller
    ##############################################################################
    def locate_last_line_of_file(self, file):
        return file.seek(-1, 2)  # Find last line of file

    ##############################################################################
    # Method: write_to_last_line_of_file
    # Purpose: Append " ') " to last line of file
    ##############################################################################
    def write_to_last_line_of_file(self, file):
        return file.write("')".encode())

    ##############################################################################
    # Method: cat_file_to_terminal
    # Purpose: Display unique bytes in terminal
    ##############################################################################
    def cat_file_to_terminal(self, cmd):
        return BOF.run_cmd(self, cmd)

    ##############################################################################
    # Method: display_unique_bytes
    # Purpose: Process unique byte pattern stored in tmp.txt and display results
    #          in terminal in an easy copy/paste manner
    ##############################################################################
    def display_unique_bytes(self):
        with open('tmp.txt', 'rb+') as read_file:  # Open file as read/binary file
            with open('tmp2.txt', 'wb+') as write_file:  # Open file in write/binary mode
                self.locate_beginning_of_file(read_file)  # Find beginning of read file
                data_buffer = self.file_buffer(read_file)  # Save data to buffer
                self.append_to_beginning_of_file(write_file, data_buffer)
                self.locate_last_line_of_file(write_file)  # Find last line of file
                self.write_to_last_line_of_file(write_file)  # Write ') to last line of file
            BOF.run_cmd(self, "cat tmp2.txt")  # Display results
            BOF.run_cmd(self, "rm tmp.txt tmp2.txt")  # Remove temporary file
            print("\n\n")

        read_file.close()
        write_file.close()

    ##############################################################################
    # Method: finding_offset
    # Purpose:
    ##############################################################################
    def get_offset(self):

        unique_bytes = self.get_bytes()

        offset = self.find_offset(
            f"/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l {self.byte_count} -q {unique_bytes} > tmp.txt")

        return offset

    ##############################################################################
    # Method: get_bytes
    # Purpose:
    ##############################################################################
    def get_bytes(self):
        while True:  # While input is not correct continue
            unique_bytes = BOF.user_input(self, 'blue', "[+] Paste unique bytes found in EIP")
            if len(str(unique_bytes)) / 2 == 4:
                return str(unique_bytes)
            else:
                print(BOF.message(self, 'bred', "\n[!] Input must be an integer"))
                continue

    ##############################################################################
    # Method: find_offset
    # Purpose:
    ##############################################################################
    def find_offset(self, pattern_offset):
        offset = ''
        print("\n")
        BOF.run_cmd(self, pattern_offset)  # Run pattern_offset.rb and output to tmp.txt
        BOF.run_cmd(self, "cat tmp.txt | awk -F ' ' '{ print$6 }' > tmp2.txt")  # Extract offset
        with open('tmp2.txt', 'r') as file:
            for line in file:
                offset = line.rstrip()

        BOF.run_cmd(self, "rm tmp.txt tmp2.txt")

        file.close()

        return offset
