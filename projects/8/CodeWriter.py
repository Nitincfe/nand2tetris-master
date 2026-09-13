from pathlib import Path
class CodeWriter:

    def __init__(self, file_path):
        self.file = open(file_path, "w")
        self.label_count = 0
        self.file_name = Path(file_path).stem


    def write_arithmetic(self, command):
        if command in ['add', 'sub', 'and', 'or']:
            self.file.write("@SP\n" \
            "AM=M-1\n"
            "D=M\n"
            "A=A-1\n")

            self.sym_dict = {"add": "+", "sub": "-", "and": "&", "or": "|"}
            self.file.write(f"M=M{self.sym_dict.get(command)}D\n")

        elif command in ['neg', 'not']:
            self.file.write("@SP\n"
                            "A=M-1\n")

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
            "A=M-1\n"
            "M=0\n"
            f"@END_LABEL_{self.label_count}\n"
            "0;JMP\n"
            f"(TRUE_LABEL_{self.label_count})\n"
            "@SP\n"
            "A=M-1\n"
            "M=-1\n"
            f"(END_LABEL_{self.label_count})\n")

            self.label_count += 1

   
    def write_push_pop(self, command, segment, index): 
        self.push_pop_dict = {"argument": "ARG", "local": "LCL",
                                      "this":"THIS",
                                      "that": "THAT", 
                                      }
        self.temp_fixed_address = int(5)

        if command == "push":
            if segment in self.push_pop_dict:
                self.file.write(f"@{index}\n"
                "D=A\n"
                f"@{self.push_pop_dict.get(segment)}\n"
                "A=D+M\n"
                "D=M\n"
                "@SP\n"
                "A=M\n"
                "M=D\n"
                "@SP\n"
                "M=M+1\n")

            elif segment == "pointer":
                if index == 0:
                    self.file.write("@THIS\n"
                                    "D=M\n"
                                    "@SP\n"
                                    "A=M\n"
                                    "M=D\n"
                                    "@SP\n"
                                    "M=M+1\n")

                if index == 1:
                    self.file.write("@THAT\n"
                                    "D=M\n"
                                    "@SP\n"
                                    "A=M\n"
                                    "M=D\n"
                                    "@SP\n"
                                    "M=M+1\n")


            elif segment == "temp":
                self.file.write(f"@{self.temp_fixed_address + index}\n"
                                "D=M\n"
                                "@SP\n"
                                "A=M\n"
                                "M=D\n"
                                "@SP\n"
                                "M=M+1\n")

            elif segment == "static":
                self.file.write(f"@{self.file_name}.{index}\n"
                                "D=M\n"
                                "@SP\n"
                                "A=M\n"
                                "M=D\n"
                                "@SP\n"
                                "M=M+1\n")

            elif segment == "constant":
                self.file.write(f"@{index}\n"
                                "D=A\n"
                                "@SP\n"
                                "A=M\n"
                                "M=D\n"
                                "@SP\n"
                                "M=M+1\n")


        elif command == "pop":
            if segment in self.push_pop_dict:
                self.file.write(f"@{index}\n"
                                "D=A\n"
                                f"@{self.push_pop_dict.get(segment)}\n"
                                "A=M\n"
                                "D=D+A\n"
                                "@R13\n"
                                "M=D\n"
                                "@SP\n"
                                "AM=M-1\n"
                                "D=M\n"
                                "@R13\n"
                                "A=M\n"
                                "M=D\n")

            elif segment == "pointer":
                if index == 0:
                    self.file.write("@SP\n"
                                    "AM=M-1\n"
                                    "D=M\n"
                                    "@THIS\n"
                                    "M=D\n")

                elif index == 1:
                    self.file.write("@SP\n"
                                    "AM=M-1\n"
                                    "D=M\n"
                                    "@THAT\n"
                                    "M=D\n")

            elif segment == "temp":
                self.file.write("@SP\n"
                                "AM=M-1\n"
                                "D=M\n"
                                f"@{self.temp_fixed_address + index}\n"
                                "M=D\n")

            elif segment == "static":
                self.file.write("@SP\n"
                                "AM=M-1\n"
                                "D=M\n"
                                f"@{self.file_name}.{index}\n"
                                "M=D\n")

                
    def close(self):
        self.file.close()


