# coding=UTF-8

import sys
import stack as s
import instructions as inst
import math

# Command: python.exe .\main.py [code]

code = list(sys.argv[1])
stack = s.Stack()

pointer = 0
truejump = pointer
falsejump = pointer
loopstart = pointer
loopend = pointer
loopcounter = -1
elsejump = pointer
endifjump = pointer
iftrue = True
while pointer < len(code):
    instruction = code[pointer]
# LITERAL
    if instruction in '0123456789ABCDEF':
        inst.LITERAL(instruction, stack)
    elif instruction in '<':
        s = ''
        temp = pointer + 1
        while code[temp] not in '>':
            s += code[temp]
            temp += 1
        inst.LITERAL(s, stack)
        pointer = temp

# STRING
    elif instruction in 'qɢʀʁɴχ':
        inst.STRING(instruction, stack)

# STACK
    elif instruction in 'cɟɲçʝjʎ':
        inst.STACK(instruction, stack)

# IO
    elif instruction in 'ɪio':
        inst.IO(instruction, stack)

# MATH
    elif instruction in 'tdθðnʃʒszrɾɹlɬɮ':
        inst.MATH(instruction, stack)

# LOGICAL
    elif instruction in 'ʈɖʂʐɳɽɻɭ':
        inst.LOGICAL(instruction, stack)

# CONTROL FLOW
    elif instruction in 'ɑɒɘeɐɛəɜœɶ':
        if instruction in 'ɐ':
            # Jump to the a-th instruction
            a = stack.pop()
            if isinstance(a, int) or isinstance(a, float):
                pointer = math.ceil(a)
            elif isinstance(a, str):
                pointer = 0
                continue
        elif instruction in 'ɑɒ':
            # truthy jump back to ɑ
            if instruction in 'ɑ':
                truejump = pointer
            if instruction in 'ɒ':
                if not stack.isEmpty():
                    a = stack.pop()
                    if (isinstance(a, int) or isinstance(a, float)) and a > 0:
                        pointer = truejump
                    elif isinstance(a, str) and a != "":
                        pointer = truejump
        elif instruction in 'ɘe':
            # falsy jump back to ɑ
            if instruction in 'ɘ':
                falsejump = pointer
            if instruction in 'e':
                if not stack.isEmpty():
                    a = stack.pop()
                if (isinstance(a, int) or isinstance(a, float)) and a <= 0:
                    pointer = falsejump
                    continue
                elif isinstance(a, str) and a == "":
                    pointer = falsejump
        elif instruction in 'œɶ':
            # Loop ceil(a) times.
            if instruction in 'ɶ':
                # Check the loop counter
                # If > 0, jump to the start of the loop
                # Else, continue
                if loopcounter > 0:
                    pointer = loopstart
                    loopcounter -= 1
            elif instruction in 'œ':
                # Set the Loop Jump location
                temp = pointer
                while code[temp] not in 'ɶ':
                    temp += 1
                loopstart = pointer - 1
                loopend = temp + 1
                # If a is truthy, execute round(a) times
                # Else, continue
                if not stack.isEmpty() and loopcounter < 0:
                    a = stack.pop()
                    if isinstance(a, str):
                        continue
                    elif math.ceil(a) > 0:
                        loopcounter = math.ceil(a) - 1
        elif instruction in 'ɛəɜ':
            # if then else
            # find the next ə and ɜ
            temp = pointer
            while code[temp] != 'ɜ':
                if code[temp] in 'ə':
                    elsejump = temp
                temp += 1
            endifjump = temp

            if instruction in 'ɛ':
                if not stack.isEmpty():
                    a = stack.pop()
                if (isinstance(a, int) or isinstance(a, float)) and a > 0:
                    iftrue = True
                elif isinstance(a, str) and a != '':
                    iftrue = True
                else:
                    iftrue = False
                    pointer = elsejump
            if instruction in 'ə':
                if iftrue:
                    pointer = endifjump
    pointer += 1
