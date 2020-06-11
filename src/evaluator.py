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
    numLoops = 0

    if debugmode:
        print("Initial Conditions:")
        print("Unvoiced:", unvoiced)
        print("Voiced:", voiced)
        print("Execution:", executionStack)
        print()

    executionDepth = 0
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
            # loop index getters and setters
            elif lex[ep].lexeme == "e":
                currentStack.append(executionStack[-1])
            elif lex[ep].lexeme == "ø":
                executionStack[-1] = currentStack.pop()
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
            print(lex[ep].lexeme)
            print("Unvoiced:", unvoiced)
            print("Voiced:", voiced)
            print("Execution:", executionStack)
            print()
        ep += 1