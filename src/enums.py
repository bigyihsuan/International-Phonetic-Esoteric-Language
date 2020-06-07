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
    ININSTRUCTION = auto()