import sys
import stack as s
import instructions as inst

# Command: python.exe .\main.py [code]
'''
Go to folder: cd "D:\Programming\GitHub Repos\International-Phonetic-Esoteric-Language\src"
Run: python.exe .\main.py ""
'''
code = list(sys.argv[1])
stack = s.Stack()

pointer = 0
truejump = pointer
falsejump = pointer
loopstart = pointer
loopend = pointer
loopcounter = -1
while pointer < len(code):
    instruction = code[pointer]
# LITERAL
    if instruction in '0123456789':
        inst.LITERAL(instruction, stack)
    elif instruction in '<':
        s = ''
        temp = pointer + 1
        while code[temp] not in '>':
            s += code[temp]
            temp += 1
        inst.LITERAL(s, stack)
        pointer = temp

# STACK
    elif instruction in 'pbʙɸβ':
        inst.STACK(instruction, stack)

# IO
    elif instruction in 'ɪio':
        inst.IO(instruction, stack)

# MATH
    elif instruction in 'tdθðnʃʒszrɾɹlɬɮ':
        inst.MATH(instruction, stack)

# CONTROL FLOW
    elif instruction in 'ɑɒɘeɐɛəɜœɶ':
        if instruction in 'ɐ':
            # Jump to the a-th instruction
            a = stack.pop()
            if isinstance(a, int) or isinstance(a, float):
                pointer = round(a)
            elif isinstance(a, str):
                pointer = 0
                continue
        if instruction in 'œɶ':
            # Loop round(a) times.
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
                loopstart = pointer
                loopend = temp
                # If a is truthy, execute round(a) times
                # Else, continue
                a = stack.pop()
                if isinstance(a, str):
                    loopcounter = 1
                elif round(a) > 0:
                    loopcounter = round(a) - 1
    pointer += 1