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
from enums import Token as T
from enums import LexState as LS
import string

class Lex:
    """
    Defines a lexeme. Contains the token, and the lexed characters.
    """
    def __init__(self, token, lexeme):
        self.token = token
        self.lexeme = lexeme

    def __eq__(self, token):
        return self.token == token

    def __ne__(self, token):
        return self.token != token

def getNextToken(source):
    """ Returns a Lex containing a token and a lexeme. Input is a text stream. """
    lexstate = LS.BEGIN
    lexeme = ""
    c = ""
    sawEscape = False
    while True:
        c = source.read(1)
        # check for EOF
        if not c:
            return Lex(T.END, "")

        if lexstate == LS.BEGIN:
            if c in string.whitespace: # ignore whitespace for now
                continue
            if c in '(': # comment
                state = LS.INCOMMENT
            lexeme = c

            if c == '"':
                lexstate = LS.INSTRING
                sawEscape = False
            elif str.isdigit(c):
                return Lex(T.DIGIT, c)
            elif c == "{":
                lexstate = LS.INNUMBER
            elif c == "<":
                lexstate = LS.INFUNCTION
            elif c == "⟨":
                lexstate = LS.INLABEL
            elif c == "[":
                lexstate = LS.INLIST
            else:
                lexstate = LS.INCOMMAND
        elif lexstate == LS.INCOMMENT:
            if c == ")":
                lexstate = LS.BEGIN
            break
        elif lexstate == LS.INSTRING:
            if sawEscape:
                sawEscape = False
                if c in "\n":
                    c = ""
                elif c in '\\\'\"abfnrtv':
                    c = "\\{}".format(c)
                lexeme += c
                break
            if c == "\\":
                sawEscape = True
                break;

            lexeme += c
            if c == '"':
                lexeme = lexeme[1:-1]
                return Lex(T.STRING, lexeme)
        elif lexstate == LS.INNUMBER:
            lexeme += c
            if c == "}":
                lexeme = lexeme[1:-1]
                return Lex(T.NUMBER, lexeme)
            if c == ".":
                lexstate = LS.INFLOAT
            elif c not in string.digits:
                return Lex(T.ERR, "Invalid character in multidigit number '{}'".format(c))
        elif lexstate == LS.INFLOAT:
            lexeme += c
            if c == "}":
                lexeme = lexeme[1:-1]
                return Lex(T.NUMBER, lexeme)
            if c not in string.digits:
                return Lex(T.ERR, "Invalid character in float number '{}'".format(c))
        elif lexstate == LS.INLIST:
            # TODO
            pass
        elif lexstate == LS.INLABEL:
            # TOOD
            pass
        elif lexstate == LS.INFUNCTION:
            # TODO
            pass
        elif lexstate == LS.INCOMMAND:
            return Lex(T.COMMAND, lexeme)
        else:
            return Lex(T.ERR, "Unknown lexer state {}".format(lexstate))
