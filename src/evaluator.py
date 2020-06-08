from enums import Token as T
from enums import EvalState as E
from instructions import executeInstruction


def evaluate(lex, lab):
    """
    Evaluates code.
    Input is a list of lexemes, and a dictionary of labels.
    Most definitions of instructions are located here.
    """
    unvoiced = []
    voiced = []
    currentStack = unvoiced

    executionStack = [] # Push next exec pointer location here when jumping
    numList = 0
    numFun = 0

    isInFunction = False
    ep = 0
    while ep < len(lex):
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
        if lex[ep].token == T.FUNNAME and lex[ep+1].token != T.FUNDEFSTART:
            executionStack.append(ep+1)
            ep = lab[lex[ep].lexeme]
            isInFunction = True
        if isInFunction and lex[ep].token == T.FUNDEFEND:
            isInFunction = False
            ep = executionStack.pop()
        ep += 1