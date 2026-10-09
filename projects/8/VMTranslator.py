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

        code_writer_instance.setFileName(raw_name)

        parser_instance = Parser.Parser(vm_file)

        while parser_instance.has_more_lines():
            parser_instance.advance()
            cmd_type = parser_instance.command_type()

            # Chapter 7 Commands
            if cmd_type == "C_ARITHMETIC":
                code_writer_instance.write_arithmetic(parser_instance.arg_1())
            elif cmd_type in ["C_PUSH", "C_POP"]:
                code_writer_instance.write_push_pop(parser_instance.command(), parser_instance.arg_1(), parser_instance.arg_2())
            
            # Chapter 8 Commands
            elif cmd_type == "C_LABEL":
                code_writer_instance.writeLabel(parser_instance.arg_1())
            elif cmd_type == "C_GOTO":
                code_writer_instance.writeGoto(parser_instance.arg_1())
            elif cmd_type == "C_IF":
                code_writer_instance.writeIf(parser_instance.arg_1())
            elif cmd_type == "C_FUNCTION":
                code_writer_instance.writeFunction(parser_instance.arg_1(), parser_instance.arg_2())
            elif cmd_type == "C_CALL":
                code_writer_instance.writeCall(parser_instance.arg_1(), parser_instance.arg_2())
            elif cmd_type == "C_RETURN":
                code_writer_instance.writeReturn()

    code_writer_instance.close()

if __name__ == "__main__":
    translate()



