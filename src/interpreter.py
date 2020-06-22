#!/usr/bin/env python3

import util as E
from util import Token as T
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

# Register
register = None

currentStack = unvoiced
otherStack = voiced

debugmode = False

if len(sys.argv) > 1:
    foundFile = -1
    for i in range(1, len(sys.argv)):
        if os.path.isfile(sys.argv[i]):
            foundFile = i

    if sys.argv[1] == "-d":
        debugmode = True

    if foundFile == -1:
        code = sys.argv[2] if debugmode else sys.argv[1]
    else:
        source = open(sys.argv[foundFile], "r")
        code = source.read()

    code += " "
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

    currentStack, otherStack = evaluate(lexemes, labels, debugmode, unvoiced, voiced, executionStack, currentStack, otherStack, register)
else:
    print("Code file not found")

