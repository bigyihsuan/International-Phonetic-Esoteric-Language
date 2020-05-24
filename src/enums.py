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

class State(Flag):
    """ Represents the interpreter state. """
    BEGIN = auto()
    INNUM = auto()
    INSTRING = auto()
    INLIST = auto()
    INCOMMENT = auto()
    INLABEL = auto()
    INFUNNAME = auto()
    INFUNDEF = auto()

