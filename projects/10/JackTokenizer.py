class JackTokenizer: 

    def __init__(self, file_path):

        self.symbol_list = []
        self.type_value_list = []
        self.symbols = set("{}()[].,;+-*/&|<>=~")


    def tokenize_line(self, line):
        tokens = []

        i = 0
        while i < len(line):
            ch = line[i]

            if ch.isspace():
                i += 1               #skip, no tokens

            elif ch in self.symbols:
                tokens.append(("symbol", ch))
                i += 1    #add symbol to the list

            elif ch.isdigit():
                text = ""
                while i < len(line) and line[i].isdigit():
                    text += line[i]
                    i += 1
                tokens.append(("integerConstant", text))

            elif ch.isalpha():
                text = ""
                while i < len(line) and line[i].isalpha():
                    text += line[i]
                    i += 1
                if text in self.keyword_list:
                    tokens.append(("keyword", text))
                else:
                    tokens.append(("integer", text))

            elif ch.isalnum() or ch == "_":
                text = ""
                while i < len(line) and line[i].isalnum() or line[i] == "_":
                    text += line[i]
                    i += 1
                tokens.append(("integer", text))

        return tokens

                    

                



        


            
            