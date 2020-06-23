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

digits = {
"0":0, "1":1,
"2":2, "3":3,
"4":4, "5":5,
"6":6, "7":7,
"8":8, "9":9,
"A":10, "a":10,
"B":11, "b":11,
"C":12, "c":12,
"D":13, "d":13,
"E":14, "e":14,
"F":15, "f":15,
"G":16, "g":16,
"H":17, "h":17,
"I":18, "i":18,
"J":19, "j":19,
"K":20, "k":20,
"L":21, "l":21,
"M":22, "m":22,
"N":23, "n":23,
"O":24, "o":24,
"P":25, "p":25,
"Q":26, "q":26,
"R":27, "r":27,
"S":28, "s":28,
"T":29, "t":29,
"U":30, "u":30,
"V":31, "v":31,
"W":32, "w":32,
"X":33, "x":33,
"Y":34, "y":34,
"Z":35, "z":35 }

# https://stackoverflow.com/a/20170279/8143168
def convert_base(s, base=10):
    ret = 0
    if "." not in s:
        bef = s
    else:
        bef, aft = s.split(".")
    for i in enumerate(reversed(bef)):
        integer = digits[i[1]]
        if integer >= base: raise ValueError
        ret += base**i[0] * integer
    if "." not in s: return ret
    for i in enumerate(aft):
        integer = digits[i[1]]
        if integer >= base: raise ValueError
        ret += base**-(i[0] + 1) * integer
    return ret