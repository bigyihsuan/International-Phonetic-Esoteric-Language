from util import Token as T
from util import LexState as LS
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
        return "<Lex: {}, {}>".format(self.token, repr(self.lexeme))

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
        if strPos == len(code):
            return ("", Lex(T.END, ""))
        else:
            c = code[strPos]

        if lexstate == LS.BEGIN:
            if c in string.whitespace:
                code = code[1:]
                strPos = 0
                continue
            lexeme = c
            start = strPos
            padding = 1 if code[strPos+1] == "\n" else 0

            if c == "(":
                lexstate = LS.INCOMMENT
            elif c == '"':
                lexstate = LS.INSTRING
                sawEscape = False
            elif str.isdigit(c):
                return (code[strPos+len(lexeme)+padding:], Lex(T.NUMBER, c))
            elif c == "{":
                lexstate = LS.INNUMBER
            elif c == "<":
                lexstate = LS.INFUNCTIONNAME
            elif c == "/":
                return (code[strPos+len(lexeme)+padding:], Lex(T.FUNDEFSTART, c))
            elif c == "\\":
                return (code[strPos+len(lexeme)+padding:], Lex(T.FUNDEFEND, c))
            elif c == "|":
                lexstate = LS.INLABEL
            elif c == "[":
                return (code[strPos+len(lexeme):], Lex(T.LISTBEGIN, lexeme))
            elif c == "]":
                return (code[strPos+len(lexeme):], Lex(T.LISTEND, lexeme))
            elif c == ".":
                return (code[strPos+len(lexeme):], Lex(T.LISTSEP, lexeme))
            elif c == "ɑ":
                return (code[strPos+len(lexeme):], Lex(T.LOOPSTART, lexeme))
            elif c == "ɒ":
                return (code[strPos+len(lexeme):], Lex(T.LOOPEND, lexeme))
            elif c == "ɛ":
                return (code[strPos+len(lexeme):], Lex(T.LOOPEXIT, lexeme))
            else:
                lexstate = LS.ININSTRUCTION

        elif lexstate == LS.INCOMMENT:
            lexeme += c
            if c == ")":
                return (code[start+len(lexeme):], Lex(T.COMMENT, lexeme))

        elif lexstate == LS.INSTRING:
            if sawEscape:
                sawEscape = False
                lexeme += c
                strPos += 1
                continue
            if c in "\\":
                sawEscape = True
                lexeme += c
                strPos += 1
                continue
            else:
                lexeme += c
            if c in '"':
                return (code[start+len(lexeme):], Lex(T.STRING, bytearray(lexeme, "utf-8").decode("unicode_escape"))) # bytearray(lexeme, "utf-8").decode("unicode_escape")

        elif lexstate == LS.INNUMBER:
            lexeme += c
            if c == "}":
                return (code[start+len(lexeme):], Lex(T.NUMBER, lexeme[1:-1].upper()))
            if c == ".":
                lexstate = LS.INFLOAT
            elif c not in string.digits + string.ascii_letters and c not in "-":
                return (code[start+len(lexeme):], Lex(T.ERR, "Invalid character in multidigit number '{}'".format(c)))

        elif lexstate == LS.INFLOAT:
            lexeme += c
            if c == "}":
                return (code[start+len(lexeme):], Lex(T.NUMBER, lexeme[1:-1].upper()))
            if c not in string.digits + string.ascii_letters:
                return (code[start+len(lexeme):], Lex(T.ERR, "Invalid character in float number '{}'".format(c)))

        elif lexstate == LS.INLABEL:
            lexeme += c
            if c == "|":
                return (code[start+len(lexeme):], Lex(T.LABEL, lexeme[1:-1]))

        elif lexstate == LS.INFUNCTIONNAME:
            if c in string.whitespace:
                return (code[start+len(lexeme):], Lex(T.ERR, "Whitespace not allowed in function name"))
            lexeme += c
            if c == ">":
                return (code[start+len(lexeme):], Lex(T.FUNNAME, lexeme[1:-1]))

        elif lexstate == LS.ININSTRUCTION:
            return (code[start+len(lexeme):], Lex(T.INSTRUCTION, lexeme))

        else:
            return (code[start+len(lexeme):], Lex(T.ERR, "Unknown lexer state {}".format(lexstate)))
        strPos += 1
