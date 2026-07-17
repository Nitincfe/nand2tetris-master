class Parser:
    def __init__(self, file_path):
        #Reading all lines from the file into memory
        with open(file_path, "r") as file:
            self.lines = file.readlines()

        self.current_line_idx = 0
        self.current_instruction = None

    def reset(self):
        self.current_line_idx = 0
        self.current_instruction = None


    def hasMoreLines(self):
        #This method returns true if the list still has lines to process 
        return self.current_line_idx < len(self.lines)
    
    #Step 2: The Advance Method

    def advance(self):
        raw_line = self.lines[self.current_line_idx]
        self.current_line_idx += 1

        clean_line = raw_line.strip().replace(" ", "")

        if "//" in clean_line:
            clean_line = clean_line.split("//")[0]
        
        self.current_instruction = clean_line

    #Step 3: The instructionType Method

    def instructionType(self):
        if not self.current_instruction:
            return "SKIP"
        
        if self.current_instruction.startswith("@"):
            return "A_INSTRUCTION"
        
        elif self.current_instruction.startswith("("):
            return "L_INSTRUCTION"
        
        else:
            return "C_INSTRUCTION"
        

    #Step  4: Getting the symbol
    def symbol(self):
        if self.instructionType() == "A_INSTRUCTION":
            return self.current_instruction[1:]
        elif self.instructionType() == "L_INSTRUCTION":
            return self.current_instruction[1:-1]
        return None
    

    #Step 5: Isolating the Symbolic Text Fields

    def dest(self):

        if "=" in self.current_instruction:
            return self.current_instruction.split("=")[0]
        return "null"
        
    def jump(self):
        if ";" in self.current_instruction:
            return self.current_instruction.split(";")[1]
        return "null"
    
    def comp(self):
        remaining = self.current_instruction

        if "=" in remaining:
            remaining = remaining.split("=")[1]

        if ";" in remaining:
            remaining = remaining.split(";")[0]

        return remaining

