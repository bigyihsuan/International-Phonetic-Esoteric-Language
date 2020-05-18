"""
This file defines the classes used for parsing, and later interpreting.

symbol = expression
{} = 0 or more
[] = 0 or 1
() = 1
"" = terminal string
| = or

Expr = Code | Comment | FunDecl
Code = {Code} (FunCall | DoLoop | CountLoop | INSTRUCTION | LIST | STRING | NUMBER) {Code}

FunDecl = "[" (NONDIG {TEXT}) "|" Code "]"
FunCaall = "[" (NONDIG {TEXT}) "]"
Comment = "(" TEXT ")"
DoLoop = "ɑ" Code "ɒ"
CountLoop = "ʌ" Code "ɔ"

INSTRUCTION = check readme for all instructions (conjump in here)
LIST = "/" {["."] NUMBER "."} {["."] STRING "."} {"." LIST "."} "/"
STRING = '"' TEXT '"'
NUMBER = DIGIT | "[" (DIGIT{DIGIT}[.]{DIGIT}) "]"
TEXT = any non-whitespace character
NONDIG = TEXT without DIGIT
DIGIT = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
"""
from enum import Flag, auto

class Token(Flag):
    ERR = auto()
    DONE = auto()
    FUNDECL = auto()
    FUNCALL = auto()
    COMMENT = auto()
    DOLOOP = auto()
    COUNTLOOP = auto()
    LIST = auto()
    STRING = auto()
    NUMBER = auto()

class Lexeme:
    """
    A class for a Lexeme.
    """
    def __init__(self):
        self.token = Token.ERR
        self.instructionNumber = -1

    def __init__(self, token, instructionNumber, lexeme):
        self.token = token
        self.instructionNumber = instructionNumber
        self.lexeme = lexeme

    def __eq__(self, other):
        return self.token == other.token

    def __ne__(self, other):
        return self.token != other.token