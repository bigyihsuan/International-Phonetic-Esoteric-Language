"""
This file defines the classes used for parsing, and later interpreting.

symbol = expression
{} = 0 or more
[] = 0 or 1
() = 1
"" = terminal string
| = or

Expr = Code | Comment | FunDecl
Code = {Code} (FunCall | DoLoop | CountLoop | LabelCreate | LabelJump | INSTRUCTION | LIST | STRING | NUMBER) {Code}

FunDecl = "<" (NONDIG {TEXT}) ">/" Code "/"
FunCall = "<" (NONDIG {TEXT}) ">"
Comment = "(" TEXT ")"
LabelCreate = "ʎ❬" TEXT "❭"
LabelJump = "ʟ❬" TEXT "❭"

INSTRUCTION = check readme for all instructions (conditional skip in here)
LIST = "[" ["."] { (NUMBER | STRING | LIST) ["."] } "]"
STRING = '"' TEXT '"'
NUMBER = DIGIT | "[" (DIGIT{DIGIT}["."]{DIGIT}) "]"
TEXT = any non-whitespace character
NONDIG = TEXT without DIGIT
DIGIT = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
"""
from enum import Flag, auto

class Token(Flag):
    ERR = auto() # Error
    DONE = auto() # When EOF reached
    # Constants
    NUMBER = auto()
    STRING = auto()
    LABEL = auto()
    LIST = auto()
    # instructions
    INSTRUCTION = auto()
    # Functions and Labels
    FUNDECL = auto()
    FUNCALL = auto()



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

class Instruction:
    """
    An interface representing an instruction.
    """
    def eval():
        """
        Called when evaluating the instruction.
        Usually will be implemented as pushes and pops, and ops.
        """
        pass

class Number(Instruction):
    """ Pushes a number """
    def __init__(self, value, stack):
        self.value = value
        self.stack = stack

    def eval(self):
        self.stack.push(self.value)
