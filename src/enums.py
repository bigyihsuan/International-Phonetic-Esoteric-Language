from enum import Flag, auto

class Token(Flag):
    BEGIN = auto()
    END = auto()
    ERR = auto()
    COMMENT = auto()
    NUMBER = auto()
    STRING = auto()
    LIST = auto()
    FUNDEF = auto()
    FUNCALL = auto()
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
    INFUNCTION = auto()
    INLABEL = auto()
    INCOMMAND = auto()

