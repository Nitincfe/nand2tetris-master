import os
import sys
from CompilationEngine import CompilationEngine

def analyze_file(jack_path):
    out_path = jack_path[:-len(".jack")] + ".xml"
    engine = CompilationEngine(jack_path, out_path)
    engine.compileClass()

def main():
    source = sys.argv[1] if len(sys.argv) > 1 else "."
    if os.path.isdir(source):
        for name in sorted(os.listdir(source)):
            if name.endswith(".jack"):
                analyze_file(os.path.join(source, name))
    elif source.endswith(".jack"):
        analyze_file(source)
    else:
        print("Usage: python JackAnalyzer.py <file.jack | folder>")

if __name__ == "__main__":
    main()