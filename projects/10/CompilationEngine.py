import JackTokenizer 


from JackTokenizer import (JackTokenizer, KEYWORD, SYMBOL,
                           IDENTIFIER, INT_CONST, STRING_CONST)

XML_ESCAPES = {"<": "&lt;", ">": "&gt;", '"': "&quot;", "&": "&amp;"}

def escape(text):
    result = ""
    for ch in text:
        result += XML_ESCAPES.get(ch, ch)
    return result


class CompilationEngine:

    def __init__(self, input_path, output_path):
        self.tokenizer = JackTokenizer(input_path)
        self.out = open(output_path, "w")
        self.tokenizer.advance()
    
    def _write_token(self):
        t = self.tokenizer.tokenType()

        if t == KEYWORD:
            tag, value = "keyword", self.tokenizer.keyWord().lower()
        elif t == SYMBOL:
            tag, value = "symbol", escape(self.tokenizer.symbol())
        elif t == IDENTIFIER:
            tag, value = "identifier", self.tokenizer.identifier()
        elif t == INT_CONST:
            tag, value = "integerConstant", self.tokenizer.intVal()
        else:
            tag, value = "stringConstant", escape(self.tokenizer.stringVal())

        self.out.write(f"<{tag}> {(value)} </{tag}>\n")

        if self.tokenizer.hasMoreTokens():
            self.tokenizer.advance()

    def compileClass(self):
        self.out.write("<class>\n")
        self._write_token()
        self._write_token()
        self._write_token()
        while (self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() in ("STATIC", "FIELD")):
            self.compileClassVarDec()
        while (self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() in ("CONSTRUCTOR", "FUNCTION", "METHOD")):
            self.compileSubroutine()
        self._write_token()
        self.out.write("</class>\n")
        self.close()



def close(self):
    self.out.close()


        
         


        

        
