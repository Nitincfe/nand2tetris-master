import Parser
import CodeWriter

def assemble(input_file, output_file):
    parser_instance = Parser.Parser(input_file)
    code_writer_instance = CodeWriter.CodeWriter(output_file)

    while parser_instance.has_more_lines():
        parser_instance.advance()

        if parser_instance.command_type() == "C_ARITHMETIC":
            code_writer_instance.write_arithmetic(parser_instance.arg_1())

        elif parser_instance.command_type() in ["C_PUSH", "C_POP"]:
            code_writer_instance.write_push_pop(parser_instance.command(), parser_instance.arg_1(), parser_instance.arg_2())

    # C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL are intentionally
        # unhandled here. Program flow and function calling belong to a later
        # NTT stage (Chapter 8). This driver currently covers arithmetic + push/pop only.
    
    code_writer_instance.close()

