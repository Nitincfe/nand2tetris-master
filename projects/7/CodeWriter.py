class CodeWriter:

    def __init__(self, file_path):
        self.file = open(file_path, "w")
        self.label_count = 0

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
            self.comp_dict = {"eq":"JEQ", "gt": "JGT", "lt": "JLT"}
            self.file.write("@SP\n" \
            "AM=M-1\n" \
            "D=M\n" \
            "A=A-1\n"
            "D=M-D\n"
            f"@TRUE_LABEL_{self.label_count}\n"
            f"D;{self.comp_dict.get(command)}\n"
            "@SP\n"
            "A=M\n"
            "M=0\n"
            f"@END_LABEL_{self.label_count}\n"
            "0;JMP\n"
            f"(TRUE_LABEL_{self.label_count})\n"
            "@SP\n"
            "A=M\n"
            "M=-1\n"
            f"(END_LABEL_{self.label_count})\n")

            self.label_count += 1

   
    def write_push_pop(self, command, segment, index): 
        self.push_pop_dict = {"argument": "ARG", "local": "LCL",
                                      "static":"", "this":"THIS",
                                      "that": "THAT", "pointer":"",
                                      "temp":"TEMP"}
        f"@{index}\n"
        "D=A\n"
        "@LCL\n"
        "A=D+M\n"
        "D=M\n"
        "@SP\n"
        "A=M\n"
        "M=D\n"
        "@SP\n"
        "M=M+1\n"