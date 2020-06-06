from enum import Flag, auto

class Token(Flag):
    BEGIN = auto()
    END = auto()
    ERR = auto()
    COMMENT = auto()
    NUMBER = auto()
    STRING = auto()
    LISTBEGIN = auto()
    LISTSEP = auto()
    LISTEND = auto()
    FUNNAME = auto()
    FUNDEF = auto()
    LABEL = auto()
    JUMP = auto()
    COMMAND = auto()
    DONE = auto()

class LexState(Flag):
    """
    Represents the interpreter state.
    """
    BEGIN = auto()
    INNUMBER = auto()
    INFLOAT = auto()
    INSTRING = auto()
    INLIST = auto()
    INCOMMENT = auto()
    INFUNCTIONNAME = auto()
    INFUNCTIONCODE = auto()
    INLABEL = auto()
    INCOMMAND = auto()

"""
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
LabelCreate = "❬" TEXT "❭"
LabelJump = "ʟ❬" TEXT "❭"

INSTRUCTION = check readme for all instructions (conditional skip in here)
LIST = "[" ["."] { (NUMBER | STRING | LIST) ["."] } "]"
STRING = '"' TEXT '"'
NUMBER = DIGIT | "[" (DIGIT{DIGIT}["."]{DIGIT}) "]"
TEXT = any non-whitespace character
NONDIG = TEXT without DIGIT
DIGIT = 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
"""

