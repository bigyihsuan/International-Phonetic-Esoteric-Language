"""
This file defines the classes used for parsing, and later interpreting.

Rules:

[MORE]

Number -> DIGIT | [NUM]
NUM -> DIGIT {DIGIT}
DIGIT -> [0-9A-Fa-f]
String -> <CHARS>
CHARS -> CHAR {CHAR}
CHAR -> [anycharacter]
"""