import Parser
import Code
from SymbolTable import SymbolTable
import sys

def assemble(input_file, output_file):
    parser_instance = Parser.Parser(input_file)
    symbol_table_instance = SymbolTable()

    # Pass 1 - Label Resolution
    rom_address = 0
    while parser_instance.hasMoreLines():
        parser_instance.advance()
        inst_type = parser_instance.instructionType()

        if inst_type == "L_INSTRUCTION": 
            label = parser_instance.symbol()
            if not symbol_table_instance.contains(label):
                symbol_table_instance.add_entry(label, rom_address)
        # FIXED: This must be aligned with the outer 'if', not nested inside it
        elif inst_type in ["A_INSTRUCTION", "C_INSTRUCTION"]:
            rom_address += 1

    # Resetting the parser pointer for Pass 2
    parser_instance.reset()

    # Pass 2 - Variable Allocation
    ram_address = 16
    with open(output_file, "w") as hack_file:
        while parser_instance.hasMoreLines():
            parser_instance.advance()
            inst_type = parser_instance.instructionType()

            if inst_type in ["SKIP", "L_INSTRUCTION"]:
                continue

            elif inst_type == "C_INSTRUCTION":
                comp_mnemonic = parser_instance.comp()
                dest_mnemonic = parser_instance.dest()
                jump_mnemonic = parser_instance.jump()

                comp_bits = Code.comp(comp_mnemonic)
                dest_bits = Code.dest(dest_mnemonic)
                jump_bits = Code.jump(jump_mnemonic)

                binary_instruction = "111" + comp_bits + dest_bits + jump_bits
                hack_file.write(binary_instruction + "\n")
            
            elif inst_type == "A_INSTRUCTION":
                raw_symbol = parser_instance.symbol()
                
                # Check if the symbol is a numeric address or a variable
                if raw_symbol.isdigit():
                    address = int(raw_symbol)
                else:
                    # If it's a new variable, assign it the next available RAM address
                    if not symbol_table_instance.contains(raw_symbol):
                        symbol_table_instance.add_entry(raw_symbol, ram_address)
                        ram_address += 1
                    address = symbol_table_instance.get_address(raw_symbol)
                        
                binary_instruction = bin(address)[2:].zfill(16)
                hack_file.write(binary_instruction + "\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python Main.py <file.asm>")
        sys.exit(1)
        
    input_file = sys.argv[1]
    output_file = input_file.replace(".asm", ".hack")
    
    assemble(input_file, output_file)