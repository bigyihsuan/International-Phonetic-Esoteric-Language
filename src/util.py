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
    FUNDEFSTART = auto()
    FUNDEFEND = auto()
    LABEL = auto()
    JUMP = auto()
    INSTRUCTION = auto()
    LOOPSTART = auto()
    LOOPEND = auto()
    LOOPEXIT = auto()
    DONE = auto()

class LexState(Flag):
    """
    Represents the lexer state.
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
    ININSTRUCTION = auto()

class EvalState(Flag):
    """
    Represents the interpreter state.
    """
    DEFAULT = auto()
    CALLING = auto()

digits = {str(k):k for k in range(10)}            # numbers
d.update({chr(k):k - 55 for k in range(65, 91)})  # uppercase alphabet
d.update({chr(k):k - 87 for k in range(97, 123)}) # lowercase alphabet

# https://stackoverflow.com/a/20170279/8143168
def convert_base(s, base=10):
    ret = 0
    if "." not in s:
        bef = s
    else:
        bef, aft = s.split(".")
    for i in enumerate(reversed(bef)):
        if i[1] in digits:
            integer = digits[i[1]]
            if integer >= base: raise ValueError
        else:
            integer = 0
        ret += base**i[0] * integer
    if "." not in s: return ret
    for i in enumerate(aft):
        integer = digits[i[1]]
        if integer >= base: raise ValueError
        ret += base**-(i[0] + 1) * integer
    if "-" in s:
        ret = -ret
    return ret
