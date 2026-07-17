class SymbolTable:
    def __init__(self):
        self.symbol_table = {
            "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
            "SCREEN": 16384, "KBD": 24576
        }
        for i in range(16):
            self.symbol_table[f"R{i}"] = i

    def add_entry(self, symbol: str, address: int) -> None:
        self.symbol_table[symbol] = address

    def contains(self, symbol: str) -> bool:
        """Returns True if the symbol is present in the symbol table"""
        return symbol in self.symbol_table

    def get_address(self, symbol: str) -> int:
        return self.symbol_table[symbol]

