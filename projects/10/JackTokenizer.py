class JackTokenizer: 

    def __init__(self, file_path):

        self.symbol_list = []
        self.type_value_list = []
        self.symbols = set("{}()[].,;+-*/&|<>=~")

        self.keyword_list = set(["class", "constructor", "function", "method",
                            "field", "static", "var",
                            "int", "char", "boolean", "void",
                            "true", "false", "null", "this",
                            "let", "do", "if", "else", "while", "return"])


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

            elif ch.isalpha() or ch == "_":
                text = ""
                while i < len(line) and (line[i].isalnum() or line[i] == "_"):
                    text += line[i]
                    i += 1
                if text in self.keyword_list:
                    tokens.append(("keyword", text))
                else:
                    tokens.append(("identifier", text))    

            elif ch == '"':
                text = ""
                i += 1
                while i < len(line) and line[i] != '"':
                    text += line[i]
                    i += 1
                tokens.append(('stringConstant', text))
                i += 1

            else: 
                i += 1

        return tokens

                    

                



        


            
            