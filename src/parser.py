from enums import Token as T
import lexer
import os

""" This file defines the code for the parser. """

class Parser:
    __pushedBack = False
    __token = None

    def getNextToken(self, code):
        if self.__pushedBack:
            self.__pushedBack = False
            return self.__token
        return lexer.getNextToken(code)

    def pushBackToken(self, token):
        if self.__pushedBack:
            os.abort()
        self.__pushedBack = True
        self.__token = token

    def mapLabels(self, lex, lab):
        """
        Maps labels and functions to their locations within the lexeme list.
        Labels point to the lexeme directly following it.
        Functions point to the start of their body.
        """
        for i in range(len(lex)):
            if i < len(lex):
                if lex[i].token == T.LABEL:
                    lab[lex[i].lexeme] = i
                elif lex[i].token == T.FUNNAME and lex[i+1].token == T.FUNDEFSTART:
                    lab[lex[i].lexeme] = i

    def validateLexemes(self, lex, lab):
        """
        Validates the order of lexemes.
        Input is a list of lexemes and a dictionary of labels.
        Returns true or false based on whether the lexeme list is valid.
        For example, the Jump instruction is needs a COMMAND with lexeme=="ʟ"
        followed by a LABEL that has been defined.
        There weill always be a 1 FUNDEDSTART to each FUNDEFEND, as well as
        LISTBEGIN and LISTEND.
        """
        funs = 0
        lists = 0
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
                if lex[i].token == T.INSTRUCTION and lex[i].lexeme == "ʟ":
                    if (lex[i+1].token != T.LABEL):
                        errors.append("Missing label after JUMP at Lex {}".format(i))
                if lex[i].token == T.LABEL:
                    if lex[i].lexeme not in lab:
                        errors.append("Label {} at {} not defined".format(lex[i].lexeme, i))
                if lex[i].token == T.FUNNAME and lex[i+1].token != T.FUNDEFSTART:
                    if lex[i].lexeme not in lab:
                        errors.append("Function call {} at {} not defined".format(lex[i].lexeme, i))
        if funs != 0:
            errors.append("Missmatched function bodies exist")
        if lists != 0:
            errors.append("Missmatched list brackets exist")

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