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

    def compileClassVarDec(self):
        self.out.write("<classVarDec>\n")
        self._write_token()
        self._write_token()
        while not (self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ";"):
            self._write_token()
        self._write_token()
        self.out.write("</classVarDec>\n")

    def compileSubroutine(self):
        self.out.write("<subroutineDec>\n")
        self._write_token()
        self._write_token()
        self._write_token()
        self._write_token()
        self.compileParameterList()
        self._write_token()
        self.compileSubroutineBody()
        self.out.write("</subroutineDec>\n")

    def compileParameterList(self):
        self.out.write("<parameterList>\n")
        while not(self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ")"):
            self._write_token()
        self.out.write("</parameterList>\n")

    def compileVarDec(self):
        self.out.write("<varDec>\n")
        while not(self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ";"):
            self._write_token()
        self._write_token()
        self.out.write("</varDec>\n")

    def compileSubroutineBody(self):
        self.out.write("<subroutineBody>\n")
        self._write_token()
        while (self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == "VAR"):
            self.compileVarDec()
        self.compileStatements()
        self._write_token()
        self.out.write("</subroutineBody>\n")

    def compileStatements(self):
        self.out.write("<statements>\n")
        while self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() in ["LET", "IF", "WHILE", "DO", "RETURN"]:
            if self.tokenizer.keyWord() == "LET":
                self.compileLet()
            elif self.tokenizer.keyWord() == "IF":
                self.compileIf()
            elif self.tokenizer.keyWord() == "WHILE":
                self.compileWhile()
            elif self.tokenizer.keyWord() == "DO":
                self.compileDo()
            elif self.tokenizer.keyWord() == "RETURN":
                self.compileReturn()
        self.out.write("</statements>\n")

    def compileReturn(self):
        self.out.write("<returnStatement>\n")
        self._write_token()
        if not (self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ";"):
            self.compileExpression()
        self._write_token()
        self.out.write("</returnStatement>\n")

    def compileDo(self):
        self.out.write("<doStatement>\n")
        self._write_token()                     
        while not (self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == "("):
            self._write_token()                  
        self._write_token()                       
        self.compileExpressionList()
        self._write_token()                    
        self._write_token()                      
        self.out.write("</doStatement>\n")

    def compileLet(self):
        self.out.write("<letStatement>\n")
        self._write_token()
        self._write_token()
        self._write_token()
        self.compileExpression()
        self._write_token()
        self.out.write("</letStatement>\n")

    def compileWhile(self):
        self.out.write("<whileStatement>\n")
        self._write_token()
        self._write_token()
        self.compileExpression()
        self._write_token()
        self._write_token()
        self.compileStatements()
        self._write_token()
        self.out.write("</whileStatement>\n")

    def compileIf(self):
        self.out.write("<ifStatement>\n")
        self._write_token()
        self._write_token()
        self.compileExpression()
        self._write_token()
        self._write_token()
        self.compileStatements()
        self._write_token()
        if self.tokenizer.tokenType() == KEYWORD and self.tokenizer.keyWord() == "ELSE":
            self._write_token()
            self._write_token()
            self.compileStatements()
            self._write_token()
        self.out.write("</ifStatement>\n")

    def compileExpression(self):
        self.out.write("<expression>\n")
        self.compileTerm()
        self.out.write("</expression>\n")

    def compileTerm(self):
        self.out.write("<term>\n")
        self._write_token()
        self.out.write("</term>\n")

    def compileExpressionList(self):
        count = 0
        self.out.write("<expressionList>\n")
        if not (self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ")"):
            self.compileExpression()
            count += 1
            while self.tokenizer.tokenType() == SYMBOL and self.tokenizer.symbol() == ",":
                self._write_token()          # the comma
                self.compileExpression()
                count += 1
        self.out.write("</expressionList>\n")
        return count

    def close(self):
        self.out.close()


        
         


        

        
