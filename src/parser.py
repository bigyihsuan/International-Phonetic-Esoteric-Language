from enums import Token as T
import lexer
import os

""" This file defines the code for the parser. """

class Parser:

    def getNextToken(self, code):
        return lexer.getNextToken(code)

    def mapLabels(self, lex, lab):
        """
        Maps labels, functions, and loops to their locations within the lexeme list.
        Labels point to the lexeme directly following it.
        Functions point to the start of their body.
        LOOP (LOOPEND) points to its associated FOR (LOOPSTART).
        EXIT (LOOPEXIT) points to the next LOOP.
        """
        loops = []
        for i in range(len(lex)):
            if lex[i].token == T.LOOPSTART:
                loops.append(i+1) # push a LOOPSTART's index
            if i < len(lex):
                if lex[i].token == T.LABEL and lex[i].lexeme not in lab:
                    if i > 0 and lex[i-1].lexeme != "ʟ":
                        lab[lex[i].lexeme] = i
                elif i+1 < len(lex):
                    if lex[i].token == T.FUNNAME and lex[i+1].token == T.FUNDEFSTART:
                        lab[lex[i].lexeme] = i+1
                    if lex[i].token == T.LOOPEND:
                        lab[i] = loops.pop() # map a loop end to its loop start

    def validateLexemes(self, lex, lab):
        """
        Validates the order of lexemes.
        Input is a list of lexemes and a dictionary of labels.
        Returns true if the lexeme list is valid.
        For example, the Jump instruction is needs a COMMAND with lexeme=="ʟ"
        followed by a LABEL that has been defined.
        There weill always be a 1 FUNDEDSTART to each FUNDEFEND, as well as LISTBEGIN and LISTEND.
        """
        funs = 0
        lists = 0
        loops = 0
        errors = []
        for i in range(len(lex)):
            if i < len(lex):
                if lex[i].token == T.FUNDEFSTART:
                    funs += 1
                if lex[i].token == T.FUNDEFEND:
                    funs -= 1
                if lex[i].token == T.LISTBEGIN:
                    lists += 1
                if lex[i].token == T.LISTEND:
                    lists -= 1
                if lex[i].token == T.LOOPSTART:
                    loops += 1
                if lex[i].token == T.LOOPEND:
                    loops -= 1
                if lex[i].token == T.INSTRUCTION and lex[i].lexeme == "ʟ":
                    if i+1 < len(lex) and lex[i+1].token != T.LABEL:
                        errors.append("Missing label after JUMP at Lex {}".format(i))
                if i+1 < len(lex):
                    if lex[i].token == T.FUNNAME and lex[i+1].token != T.FUNDEFSTART:
                        if lex[i].lexeme not in lab:
                            errors.append("Function call {} at {} not defined".format(lex[i].lexeme, i))
        if funs != 0:
            errors.append("Missmatched function bodies exist")
        if lists != 0:
            errors.append("Missmatched list brackets exist")
        if loops != 0:
            errors.append("Missmatched FORs and LOOPs exist")
        if lex[i].token == T.LABEL:
            if lex[i].lexeme not in lab:
                errors.append("Label {} at {} not defined".format(lex[i].lexeme, i))

        if len(errors) > 0:
            for e in errors:
                print(e)
        return len(errors) == 0
"""
symbol = expression
{} = 0 or more
[] = 0 or 1
() = 1
"" = terminal string
| = or

Program = Code {Code}
Code = COMMENT | FunDef | FunCall | LABEL | Jump | INSTRUCTION | Literal
FunDef = FUNNAME FunBody
FunBody = FUNDEFSTART Code FUNDEFEND
FunCall = FUNNAME
Jump = "ʟ" LABEL
INSTRUCTION
List = LISTBEGIN {Literal LISTSEP} LISTEND
Literal = NUMBER | STRING | List
"""