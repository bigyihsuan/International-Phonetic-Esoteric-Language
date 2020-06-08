import enums as E
from enums import Token as T
import sys
import io
import lexer
from parser import Parser as P
from evaluator import evaluate
import os

labels = {} # Maps a  label to a location in code.
            # Also maps the name of a function to its definition location.
lexemes = [] # List of lexemes.
parser = P()

# Stacks
unvoiced = []
voiced = []
executionStack = []

debugmode = False

if (len(sys.argv) >= 1):
    foundFile = -1
    for i in range(1, len(sys.argv)):
        if os.path.isfile(sys.argv[i]):
            foundFile = i
    if foundFile == -1:
        print("ERROR: IPEL code file not found")
    else:
        if sys.argv[1] == "-d":
            debugmode = True

        with open(sys.argv[foundFile], "r") as source:
            code = source.read() + " "

            lastlex = lexer.Lex(T.BEGIN, "")
            while lastlex.token != T.END:
                code, lex = parser.getNextToken(code)
                if (lex.token != T.COMMENT):
                    lexemes.append(lex)
                lastlex = lex
                if lastlex.token == T.ERR:
                    print("LEXING ERROR:", lastlex.lexeme)
                    os.abort()

            parser.mapLabels(lexemes, labels)
            if debugmode:
                print("Lexemes:", lexemes)
                print("Label Mapping:", labels)

            if not parser.validateLexemes(lexemes, labels):
                os.abort()
            evaluate(lexemes, labels, debugmode, unvoiced, voiced, executionStack)
else:
    print("")

