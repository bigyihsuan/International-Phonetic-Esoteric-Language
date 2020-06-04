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
    """
    Represents the interpreter state.
    """
    BEGIN = auto()
    END = auto()

    COMMENT = auto()

    """
    States representing numbers:
    DIGIT = [0-9]
    MULTIDIGIT = {[0-9]+}
    FLOAT = {[0-9]+(\.[0-9]+)+}
    """
    DIGIT = auto()
    MULTIDIGIT = auto()
    FLOAT = auto()

    STRING = auto()
    LIST = auto()

    LABEL = auto()
    FUNNAME = auto()
    FUNDEF = auto()

    """
    Represents the 'default' state the interpreter is in while parsing.
    If it is not in one of the above, it is in this.
    """
    COMMAND = auto()

    """
    Error state.
    """
    ERR = auto()

