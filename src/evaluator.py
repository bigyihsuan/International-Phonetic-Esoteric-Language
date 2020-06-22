from util import Token as T
from util import EvalState as E
from util import convert_base
from instructions import executeInstruction

import math


def evaluate(lex, lab, debugmode, unvoiced, voiced, executionStack, currentStack, otherStack, register):
    """
    Evaluates code.
    Input is a list of lexemes, and a dictionary of labels.
    Most definitions of instructions are located here.
    Returns the current stack and the other stack as a tuple (current, other).
    """

    numList = 0
    numFun = 0
    numLoops = 0

    if debugmode:
        print("Initial Conditions:")
        print("Unvoiced:", unvoiced)
        print("Voiced:", voiced)
        print("Execution:", executionStack)
        print("Register:", register)
        print()

    executionDepth = 0
    ep = 0
    while ep < len(lex):
        if debugmode:
            print(ep, lex[ep].token, repr(lex[ep].lexeme))

        otherStack = voiced if currentStack == unvoiced else unvoiced

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
                truthy = False
                con = currentStack.pop()
                if type(con) in [int, float]:
                    truthy = con != 0
                elif type(con) in [str]:
                    truthy = con != ""
                elif type(con) in [list]:
                    truthy = con != []
                ep += 1 if truthy else 0
            # loop index getters and setters
            elif lex[ep].lexeme == "e":
                if numLoops > 0:
                    currentStack.append(executionStack[-1])
            elif lex[ep].lexeme == "ø":
                if numLoops > 0:
                    executionStack[-1] = currentStack.pop()
            # voicing
            elif lex[ep].lexeme == "ɸ":
                currentStack = unvoiced
                otherStack = voiced
            elif lex[ep].lexeme == "β":
                currentStack = voiced
                otherStack = unvoiced
            elif lex[ep].lexeme == "ɓ":
                currentStack.pop(1 if currentStack == unvoiced else 0)
            elif lex[ep].lexeme == "k":
                otherStack.append(currentStack.pop())
            elif lex[ep].lexeme == "g":
                currentStack.append(otherStack.pop())
            # Register instructions
            elif lex[ep].lexeme == "w":
                register = currentStack.pop()
            elif lex[ep].lexeme == "ʍ":
                currentStack.append(register)
            else:
                executeInstruction(lex[ep].lexeme, unvoiced, voiced, currentStack)

        if ep+1 < len(lex):
            # Function jumps
            if lex[ep].token == T.FUNNAME and lex[ep+1].token != T.FUNDEFSTART:
                executionStack.append(ep)
                ep = lab[lex[ep].lexeme]
                executionDepth += 1
            if lex[ep].token == T.FUNNAME and lex[ep+1].token == T.FUNDEFSTART:
                while lex[ep].token != T.FUNDEFEND:
                    ep += 1

            # Loop jumps
            if lex[ep].token == T.LOOPSTART:
                # push to execution stack the end and start
                start = currentStack.pop() # start/index
                end = currentStack.pop() # end
                executionStack.append(end)
                executionStack.append(start)
                numLoops += 1
            if lex[ep].token == T.LOOPEND:
                if numLoops > 0:
                    if executionStack[-1] < executionStack[-2]: # jump to loop start if index < end
                        ep = lab[ep]-1 # get the loop start based on the current execution pointer
                    else:
                        executionStack.pop()
                        executionStack.pop()
                        numLoops -= 1
            if lex[ep].token == T.LOOPEXIT:
                if numLoops > 0:
                    # find the next LOOPEXIT in the label mappings
                    for i in range(ep, len(lex)):
                        if i in lab:
                            ep = lab[i] # move execution to past the loop end
                            # clean up execution stack
                            executionStack.pop()
                            executionStack.pop()
                            numLoops -= 1
                            break


        if executionDepth > 0 and lex[ep].token == T.FUNDEFEND:
            executionDepth -= 1
            ep = executionStack.pop()


        if debugmode:
            if currentStack == unvoiced:
                print("Unvoiced:", unvoiced, "<-- currentStack")
                print("Voiced:", voiced)
            else:
                print("Unvoiced:", unvoiced)
                print("Voiced:", voiced, "<-- currentStack")
            print("Execution:", executionStack)
            print("Register:", register)
            print()
        ep += 1
    return (currentStack, otherStack)