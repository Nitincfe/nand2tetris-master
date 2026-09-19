import os
import sys
import Parser
import CodeWriter


def translate():
    #Block 1: Validating the script has only one target argument  
    if len(sys.argv) != 2:
        print("Usage: python VMTranslator.py <file.vm or directory_path>")
        return
    input_path = sys.argv[1]

    #Block 2: Determining if it's a single file or a complete folder,
    #Set an output file name
    #build a list of all .vm files that need translation 
    if os.path.isdir(input_path):
        dir_name = os.path.basename(os.path.normpath(input_path))
        out_path = os.path.join(input_path, f"{dir_name}.asm")
        vm_files = [os.path.join(input_path, f) for f in os.listdir(input_path) if f.endswith(".vm")]
    else:
        out_path = input_path.replace(".vm", ".asm")
        vm_files = [input_path]

    #Block 3: Opening the output file exactly once, outside the file loop
    code_writer_instance = CodeWriter.CodeWriter(out_path)
    code_writer_instance.writeInit()

    #Block 4: Iterating through every .vm file found
    for vm_file in vm_files:
        raw_name = os.path.basename(vm_file).replace(".vm", "")




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
