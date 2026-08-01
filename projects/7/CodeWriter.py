class CodeWriter:

    def __init__(self, file_path):
        self.file = open(file_path, "w")

    def write_arithmetic(self, command):
        if command in ['add', 'sub', 'and', 'or']:
            self.file.write("@SP\n" \
            "AM=M-1\n"
            "D=M\n"
            "A=A-1\n")

            sym_dict = {"add": "+", "sub": "-", "and": "&", "or": "|"}
            self.file.write(f"M=M{sym_dict.get(command)}D\n")

        elif command in ['neg', 'not']:
            self.file.write("@SP\n"
                            "AM=M-1\n")

            neg_not_dict = {"neg":"-", "not":"!"}
            self.file.write(f"M={neg_not_dict.get(command)}M\n")

        elif command in ["eq", "gt", "lt"]:
            self.file.write("@SP\n" \
            "AM=M-1\n" \
            "D=M\n" \
            "A=A-1\n"
            "D=D-M\n"
            "O;JMP\n")

        
            