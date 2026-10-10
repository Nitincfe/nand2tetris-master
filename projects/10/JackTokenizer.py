import os
import sys

# token types. not strictly needed, but a good way to catch typos
KEYWORD, SYMBOL, IDENTIFIER, INT_CONST, STRING_CONST = (
    "KEYWORD", "SYMBOL", "IDENTIFIER", "INT_CONST", "STRING_CONST")

#the JackTokenizer
#Does three main things
#Ignores all the comments and white space in the input stream
#enables accessing the input one token at a time
#parses and provides the type of each token

class JackTokenizer:
    KEYWORDS = set(["class", "constructor", "function", "method",
        "field", "static", "var",
        "int", "char", "boolean", "void",
        "true", "false", "null", "this",
        "let", "do", "if", "else", "while", "return"])

    SYMBOLS = set("{}()[].,;+-*/&|<>=~")

    def __init__(self, file_path):
        """opens the .jack file and gets ready to tokenize it"""
        self.in_comment = False
        self.tokens = []
        with open(file_path) as f:
            for line in f:
                self.tokens.extend(self._tokenize_line(line))
        self.index = -1      #a position marker for the token list
        self.current = None  # no current token initially 


    #scanning
    def _tokenize_line(self, line):
        tokens = []
        i = 0

        if self.in_comment:         #only does anything if the line is still in comment
            end = line.find("*/")
            if end == -1:
                return tokens
            self.in_comment = False
            i = end + 2

        while i < len(line):
            ch = line[i]

            if ch.ispace():
                i += 1

            elif line.startswith("//", i):
                break 

            elif line.startswith("*/", i):
                end = line.find("/*", i + 2)
                if end == -1:
                    self.in_comment = True
                    break
                i = end + 2

            elif ch in self.SYMBOLS:           #checking if the character is a symbol
                tokens.append((SYMBOL, ch))
                i += 1


            elif ch.isdigit():             #checking digit and if there are multiple digits
                text = ""
                while i < len(line) and line[i].isdigit():
                    text += line[i]
                i += 1
                tokens.append((INT_CONST, text))

            






                



        


            
            