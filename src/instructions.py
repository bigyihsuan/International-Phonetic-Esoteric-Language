import math, string

def executeInstruction(instruction, unvoiced, voiced, currentStack):
    """
    This file defines the majority of 1-character instructions in IPEL.
    Input is an instruction, the 2 stacks, and the current stack.
    This will look at the instruction and apply it to the current stack.
    The voiced/unvoiced stacks are for the stack-switching instructions.
    """

# Stack Operations
    if instruction == "p":
        currentStack.pop()
    elif instruction == "b":
        currentStack.append(currentStack[-1])
    elif instruction == "t":
        currentStack.append(len(currentStack))
    elif instruction == "d":
        temp = currentStack[-1]
        currentStack[-1] = currentStack[-2]
        currentStack[-2] = temp
    elif instruction == "ʈ":
        a = currentStack[-1]
        b = currentStack[-2]
        c = currentStack[-3]
        currentStack[-1] = b
        currentStack[-2] = c
        currentStack[-3] = a
    elif instruction == "ɖ":
        a = currentStack[-1]
        b = currentStack[-2]
        c = currentStack[-3]
        currentStack[-1] = c
        currentStack[-2] = a
        currentStack[-3] = b
    elif instruction == "c":
        ints = list(filter(lambda x: type(x) == int, currentStack))
        strs = list(filter(lambda x: type(x) == str, currentStack))
        lsts = list(filter(lambda x: type(x) == list, currentStack))
        ints.sort()
        strs.sort()
        currentStack = lsts + strs + ints
    elif instruction == "ɟ":
        currentStack.reverse()

# Comparisons and Logical Operators
    elif instruction == "ɨ":
        if type(currentStack[-1]) != list and type(currentStack[-2]) != list:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(1 if a > b else 0)
    elif instruction == "ʉ":
        if type(currentStack[-1]) != list and type(currentStack[-2]) != list:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(1 if a >= b else 0)
    elif instruction == "ə":
        if type(currentStack[-1]) == type(currentStack[-2]):
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(1 if a == b else 0)
    elif instruction == "ɘ":
        if type(currentStack[-1]) != list and type(currentStack[-2]) != list:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(1 if a < b else 0)
    elif instruction == "ɵ":
        if type(currentStack[-1]) != list and type(currentStack[-2]) != list:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(1 if a <= b else 0)
    elif instruction == "ɜ":
        if type(currentStack[-1]) != list and type(currentStack[-2]) != list:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(1 if a and b else 0)
    elif instruction == "ɞ":
        if type(currentStack[-1]) != list and type(currentStack[-2]) != list:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(1 if a or b else 0)
    elif instruction == "ɐ":
        if type(currentStack[-1]) != list:
            a = currentStack.pop()
            currentStack.append(1 if not a else 0)

# Mathematics
    elif instruction == "s":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(a + b)
    elif instruction == "z":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(a - b)
    elif instruction == "f":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(a * b)
    elif instruction == "v":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            quotient = a / b if b != 0 else 0
            currentStack.append(quotient)
    elif instruction == "ⱱ":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(a % b)
    elif instruction == "ʃ":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(math.pow(a, b))
    elif instruction == "ʒ":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(math.log(b, a))
    elif instruction == "θ":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(a >> b)
    elif instruction == "ð":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(a << b)
    elif instruction == "ʂ":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(a & b)
    elif instruction == "ʐ":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(a | b)
    elif instruction == "r":
        if type(currentStack[-1]) in [int,float]:
            a = currentStack.pop()
            currentStack.append(~a)
    elif instruction == "ɾ":
        if type(currentStack[-1]) in [int,float]:
            a = currentStack.pop()
            currentStack.append(-a)
    elif instruction == "ɽ":
        if type(currentStack[-1]) in [int,float]:
            a = currentStack.pop()
            currentStack.append(math.ceil(a))
    elif instruction == "ʙ":
        if type(currentStack[-1]) in [int,float]:
            a = currentStack.pop()
            currentStack.append(math.floor(a))
    elif instruction == "ɬ":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(max(a,b))
    elif instruction == "ɮ":
        if type(currentStack[-1]) in [int,float] and type(currentStack[-2]) in [int,float]:
            b = currentStack.pop()
            a = currentStack.pop()
            currentStack.append(min(a,b))

# List and String Operations
    elif instruction == "x":
        if type(currentStack[-1]) in [int,float,str]:
            b = str(currentStack.pop())
        else:
            b = currentStack.pop()
        if type(currentStack[-1]) in [int,float,str]:
            a = str(currentStack.pop())
        else:
            a = currentStack.pop()
        currentStack.append(list(a)+list(b))
    elif instruction == "ɣ":
        if type(currentStack[-1]) in [int,float]:
            l = []
            n = math.ceil(currentStack.pop())
            for i in range(n):
                l.append(currentStack.pop())
            l.reverse()
            currentStack.append(l)
    elif instruction == "ħ":
        currentStack.append(len(currentStack[-1]))
    elif instruction == "ʀ":
        l = list(currentStack.pop())
        for e in l:
            currentStack.append(e)
    elif instruction == "h":
        if type(currentStack[-1]) in [int,float]:
            n = math.ceil(currentStack.pop())
            l = currentStack[-1]
            currentStack.append(l[n])
    elif instruction == "χ":
        if type(currentStack[-1]) in [int,float]:
            currentStack.append(chr(math.ceil(currentStack.pop())))
    elif instruction == "ʁ":
        if type(currentStack[-1]) == str:
            for c in currentStack.pop():
                currentStack.append(ord(c))
        if type(currentStack[-1]) == list:
            try:
                if len(list(filter(lambda x: len(x) == 1 and type(x) == str, currentStack[-1]))) > 0:
                    for c in currentStack.pop():
                        currentStack.append(ord(c))
            except Exception:
                return
    elif instruction == "ʕ":
        out = ""
        if type(currentStack[-1]) == list:
            for e in currentStack.pop():
                out += str(e)
        currentStack.append(out)
# IO
    elif instruction == "i":
        currentStack.append(input().strip())
    elif instruction == "y":
        ele = input().strip().split()
        for e in ele:
            currentStack.append(e)
    elif instruction == "ɪ":
        ele = input()
        try:
            if "{" in ele[0] and "}" in ele[-1]:
                ele = eval(ele[1:-1])
            elif ele in string.digits:
                ele = eval(ele)
            elif "[" in ele[0] and "]" in ele[-1]:
                o = []
                inNum, inStr, inList = False, False, False
                numList = 0
                n, s, l = "", "", ""
                for i,c in enumerate(ele):
                    if not inNum and not inStr and not inList:
                        if c in "{":
                            inNum = True
                        elif c in '"':
                            inStr = True
                            s += c
                        elif c in "[":
                            inList = True
                            numList += 0
                        elif c in string.digits:
                            o.append(c)
                    if inNum and not inList:
                        if c in string.digits or c in ".":
                            n += c
                        elif c in "}":
                            o.append(eval(n))
                            n = ""
                            inNum = False
                    elif inStr and not inList:
                        s += c
                        if c in '"':
                            s = bytearray(s+c, "utf-8").decode("unicode_escape")
                            o.append(eval(s))
                            inStr = False
                    elif inList:
                        if c in "[":
                            l += c
                            numList += 1
                        elif not inStr and c in "]" and numList > 0:
                            l += c
                            numList -= 1
                        elif not inNum and not inStr and c in ".":
                            l += ","
                        elif c in "{":
                            inNum = True
                        elif inNum:
                            if c in "}":
                                l += ""
                                inNum = False
                            else:
                                l += c
                        else:
                            l += c
                if l != "": # not sure what happened here
                    ele = eval(l)
                else:
                    ele = o
            elif '"' in ele[0] and '"' in ele[-1]:
                ele = eval(ele)
            else:
                ele = ele
        except:
            pass
        finally:
            currentStack.append(ele)
    elif instruction == "o":
        print(currentStack.pop())
    elif instruction == "ɤ":
        out = ""
        if type(currentStack[-1]) == list:
            for e in currentStack.pop():
                out += str(e)
        print(out)
    elif instruction == "u":
        print(currentStack.pop(), end='')
    elif instruction == "ɯ":
        trail = currentStack.pop()
        ele = currentStack.pop()
        print(ele, end=trail)