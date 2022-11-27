#!/usr/bin/env python3

import util as E
from util import Token as T
import sys
import io
import lexer
from parser import Parser as P
from evaluator import evaluate
import os

def printUsage():
    print("Usage:")
    print("python3 interpreter.py (options) (code)")
    print()
    print("Options:")
    print("    -d:          Debug mode. Print label mappings, parsed lexemes, data stack, and execution stacks.")
    print("    -f filename: Use the file `filename` as the code source input.")

def main():
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
    usingfile = -1

    if len(sys.argv) > 1:
        foundFile = -1
        for i, arg in enumerate(sys.argv):
            if arg == "-d":
                debugmode = True
            if arg == "-f":
                usingfile = i

        if usingfile > -1 and len(sys.argv) > usingfile + 1:
            source = open(sys.argv[usingfile + 1], "r")
            code = source.read()
        elif usingfile != -1:
            print("not enough arguments for using file")
            printUsage()
            return
        else:
            code = sys.argv[len(sys.argv)-1]

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
        printUsage()

if __name__ == "__main__":
    main()