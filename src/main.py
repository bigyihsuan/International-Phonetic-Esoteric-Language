import sys
import string
import stack as s

codePath = sys.argv[1] if (sys.argv[1] != None) else sys.argv[0] # python.exe .\main.py [code path]
codeFile = open(codePath, 'r', encoding="UTF-8")
code = ""
dataStack = s.Stack()

def parse(instruction, pointer, stack, code, flag=""):
    print(instruction)
    # number literals
    if (instruction in string.digits):
        stack.push(instruction)
    # string literals
    elif (instruction in '<'):
        start = pointer + 1
        tempPointer = pointer
        while (code[tempPointer] not in '>'):
            tempPointer += 1
        end = tempPointer
        literal = code[start + 1 : end]
        for char in literal:
            stack.push(ord(char))
        pointer = end + 1
    # control flow
    elif (instruction in 'ɑɒɘeɛəɜœɶ'):
        # truthy-jump
        if (instruction in 'ɑɒ'):
            start = pointer
            if (instruction in 'ɒ'):
                peek = stack.peek()
                end = pointer
                """ TODO: IMPLEMENT TRUTHY-JUMP """
    elif (instruction in '!ʘ'):
        if (instruction in '!'):
            print("Give input: ")
            inp = sys.stdin.read(1)
            if (inp in string.digits):
                stack.push(inp)
            else:
                stack.push(ord(inp))
        elif (instruction in 'ʘ'):
            print(chr(stack.pop()))
    else:
        print("instruction not found: " + instruction)
    return pointer

for line in codeFile:
    code = code + line.strip(string.whitespace)
print(code)
pointer = 0
# parse code for instructions
while (pointer < len(code)):
    instruction = code[pointer]
    pointer = parse(instruction, pointer, dataStack, code)
    pointer += 1