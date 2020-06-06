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

    def __repr__(self):
        return "<Lex: {}, {}>".format(self.token, self.lexeme)

def getNextToken(code):
    """ Input is a string.
        Output is a tuple containing:
            The input string, with the lexed substring removed, and
            a Lex containing a token and its associated lexeme """
    lexstate = LS.BEGIN
    lexeme = ""
    c = ""
    sawEscape = False
    strPos = 0
    while True:
        c = code[strPos]
        start = strPos
        # check for EOF
        if c == "":
            return (code[start+len(lexeme):], Lex(T.END, ""))

        if lexstate == LS.BEGIN:
            if c in string.whitespace:
                continue

            lexeme = c
            if c == "(": # comment
                state = LS.INCOMMENT
            elif c == '"':
                lexstate = LS.INSTRING
                sawEscape = False
            elif str.isdigit(c):
                return (code[start+len(lexeme):], Lex(T.NUMBER, c))
            elif c == "{":
                lexstate = LS.INNUMBER
            elif c == "<":
                lexstate = LS.INFUNCTIONNAME
            elif c == "/":
                lexstate = LS.INFUNCTIONCODE
            elif c == "⟨":
                lexstate = LS.INLABEL
            elif c == "[":
                return (code[start+len(lexeme):], Lex(T.LISTBEGIN, lexeme))
            elif c == "]":
                return (code[start+len(lexeme):], Lex(T.LISTEND, lexeme))
            elif c == ".":
                return (code[start+len(lexeme):], Lex(T.LISTSEP, lexeme))
            else:
                lexstate = LS.INCOMMAND

        elif lexstate == LS.INCOMMENT:
            lexeme += c
            if c == ")":
                return (code[start+len(lexeme):], Lex(T.COMMENT, lexeme[1:-1]))
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
                return (code[start+len(lexeme):], Lex(T.STRING, lexeme[1:-1]))

        elif lexstate == LS.INNUMBER:
            lexeme += c
            if c == "}":
                return (code[start+len(lexeme)+2:], Lex(T.NUMBER, lexeme[1:-1]))
            if c == ".":
                lexstate = LS.INFLOAT
            elif c not in string.digits:
                return (code[start+len(lexeme):], Lex(T.ERR, "Invalid character in multidigit number '{}'".format(c)))

        elif lexstate == LS.INFLOAT:
            lexeme += c
            if c == "}":
                return (code[start+len(lexeme):], Lex(T.NUMBER, lexeme[1:-1]))
            if c not in string.digits:
                return (code[start+len(lexeme):], Lex(T.ERR, "Invalid character in float number '{}'".format(c)))

        elif lexstate == LS.INLABEL:
            lexeme += c
            if c == "⟩":
                return (code[start+len(lexeme):], Lex(T.LABEL, lexeme[1:-1]))

        elif lexstate == LS.INFUNCTIONNAME:
            if c in string.whitespace:
                return (code[start+len(lexeme):], Lex(T.ERR, "Whitespace not allowed in function name"))
            lexeme += c
            if c == ">":
                return (code[start+len(lexeme):], Lex(T.FUNNAME, lexeme[1:-1]))

        elif lexstate == LS.INFUNCTIONCODE:
            lexeme += c
            if c == "\\":
                return (code[start+len(lexeme):], Lex(T.FUNDEF, lexeme[1:-1]))

        elif lexstate == LS.INCOMMAND:
            return (code[start+len(lexeme):], Lex(T.COMMAND, lexeme))

        else:
            return (code[start+len(lexeme):], Lex(T.ERR, "Unknown lexer state {}".format(lexstate)))
        strPos += 1
        print("DEBUG", lexeme)
