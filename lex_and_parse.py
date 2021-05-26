from Lexical_Analyzer.lexical_analyzer import lexer
from Syntax_Analyzer.syntax_analyzer import parser
import sys

if len(sys.argv) != 1:
    lexer(sys.argv[1])
    parser(sys.argv[1])
else:
    print("Please input file path")