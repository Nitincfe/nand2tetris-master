import JackTokenizer as tokenizer 

XML_ESCAPES = {"<": "&lt;", ">": "&gt;", '"': "&quot;", "&": "&amp;"}

def escape(text):
    result = ""
    for ch in text:
        result += XML_ESCAPES.get(ch, ch)
    return result


class CompilationEngine:

    def __init__(self, input_file, output_file):
        for 
        
    
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


        
         


        

        
