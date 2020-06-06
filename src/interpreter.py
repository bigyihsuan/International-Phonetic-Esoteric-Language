import enums as E
from enums import Token as T
import sys
import io
import lexer

unvoicedStack = []
voicedStack = []

labels = {} # Maps a  label to a location in code.
            # Also maps the name of a function to its location.
lexemes = [] # List of lexemes.

executionStack = []

stderr = sys.stderr

if (len(sys.argv) == 1):
    # Take code from stdin
    source = sys.stdin
else:
    # Take code from the given file
    source = open(sys.argv[1], "r")

code = source.read() + " "

lastlex = lexer.Lex(T.BEGIN, "")
lexemes.append(lastlex)
while lastlex.token != T.END:
    code, lex = lexer.getNextToken(code)
    lexemes.append(lex)
    lastlex = lex
    if lastlex.token == T.ERR:
        print("LEXING ERROR:", lastlex.lexeme)
        break

for l in lexemes:
    print(l)