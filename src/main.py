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
        inst.LITERAL(instruction, stack)
        pointer = temp + 1
# IO
    elif instruction in 'ɪio':
        inst.IO(instruction, stack)

    pointer += 1