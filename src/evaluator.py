from enums import Token as T
from enums import EvalState as E
from instructions import executeInstruction


def evaluate(lex, lab, debugmode, unvoiced, voiced, executionStack):
    """
    Evaluates code.
    Input is a list of lexemes, and a dictionary of labels.
    Most definitions of instructions are located here.
    """
    currentStack = unvoiced

    numList = 0
    numFun = 0

    if debugmode:
        print("Initial Conditions:")
        print("Unvoiced:", unvoiced)
        print("Voiced:", voiced)
        print("Execution:", executionStack)
        print()

    isInFunction = False
    ep = 0
    while ep < len(lex):
        if debugmode:
            print(ep, lex[ep].token)

        if lex[ep].token == T.NUMBER:
            if "." in lex[ep].lexeme: # number is a float
                currentStack.append(float(lex[ep].lexeme))
            else:
                currentStack.append(int(lex[ep].lexeme))
        if lex[ep].token == T.STRING:
            currentStack.append(lex[ep].lexeme[1:-1])
        if lex[ep].token == T.LISTBEGIN:
            numList = 1
            list = "["
            while numList > 0:
                ep += 1
                list += lex[ep].lexeme if lex[ep].token != T.LISTSEP else ","
                if lex[ep].token == T.LISTBEGIN:
                    numList += 1
                if lex[ep].token == T.LISTEND:
                    numList -= 1
            currentStack.append(eval(list))

        if lex[ep].token == T.INSTRUCTION:
            if lex[ep].lexeme == "ʟ": # Unconditional jump
                ep = lab[lex[ep+1].lexeme]
            elif lex[ep].lexeme == "ʌ": # Conditional skip
                ep += 1 if currentStack.pop() else 0
            else:
                executeInstruction(lex[ep].lexeme, unvoiced, voiced, currentStack)

        # Function jumps
        if ep+1 < len(lex):
            if lex[ep].token == T.FUNNAME and lex[ep+1].token != T.FUNDEFSTART:
                executionStack.append(ep)
                ep = lab[lex[ep].lexeme]
                isInFunction = True
            if lex[ep].token == T.FUNNAME and lex[ep+1].token == T.FUNDEFSTART:
                while lex[ep].token != T.FUNDEFEND:
                    ep += 1
        if isInFunction and lex[ep].token == T.FUNDEFEND:
            isInFunction = False
            ep = executionStack.pop()

        if debugmode:
            print(lex[ep].lexeme)
            print("Unvoiced:", unvoiced)
            print("Voiced:", voiced)
            print("Execution:", executionStack)
            print()
        ep += 1