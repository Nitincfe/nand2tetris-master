class Parser:

    def __init__(self, file_path):
        self.lines = []
        self.split_current_instruction = []
        #Reading all lines from the file into memory
        with open(file_path, "r") as file:
            for line in file:
                #Strip comments and surrounding whitespace
                clean_line = line.split("//")[0].strip()
                if clean_line:
                    self.lines.append(clean_line)


        self.current_line_idx = 0
        self.current_instruction = None

    def has_more_lines(self):
        #Checking if there are more lines in the input
        return self.current_line_idx < len(self.lines)

    def advance(self):
        self.current_instruction = self.lines[self.current_line_idx]
        self.current_line_idx += 1
        #Splitting the current instruction for command type, arg1, and arg2
        self.split_current_instruction = self.current_instruction.split()

    def command_type(self):
        if self.split_current_instruction[0] in ('add', 'sub', 'neg', 'eq',
                                              'gt', 'lt', 'and', 'or',
                                              'not'):
            return "C_ARITHMETIC"
        
        elif self.split_current_instruction[0] == "push":
            return "C_PUSH"

        elif self.split_current_instruction[0] == "pop":
            return "C_POP"
        
        elif self.split_current_instruction[0] == "function":  
            return "C_FUNCTION"       

        elif self.split_current_instruction[0] == "return":  
            return "C_RETURN"    

        elif self.split_current_instruction[0] == "call":  
            return "C_CALL"   

        elif self.split_current_instruction[0] == "label":  
            return "C_LABEL"   

        elif self.split_current_instruction[0] == "goto":  
            return "C_GOTO"   

        elif self.split_current_instruction[0] == "if-goto":  
            return "C_IF"  
        else: 
            raise ValueError(f"Unknown command: {self.split_current_instruction[0]}") 
                           
    def command(self):
        return self.split_current_instruction[0]

    def arg_1(self):
        if self.command_type() == "C_RETURN":
            return "SKIP"
        elif self.command_type() == "C_ARITHMETIC":
            return self.split_current_instruction[0]
        return self.split_current_instruction[1]

    def arg_2(self):
        if self.command_type() in ('C_ARITHMETIC', 'C_LABEL', 'C_GOTO',
                                   'C_IF', 'C_RETURN'):
            return "SKIP"
        return int(self.split_current_instruction[2])
        