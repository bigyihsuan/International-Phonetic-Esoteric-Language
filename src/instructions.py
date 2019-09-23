def LITERAL(instruction, stack):
    if (str.isdigit(instruction)):
        stack.push(int(instruction))
    else:
        stack.push(instruction)

def STACK(instruction, stack):
    if instruction in 'p':
        stack.pop()
    elif instruction in 'b':
        stack.push(stack.peek())
    elif instruction in 'ʙ':
        a = stack[0]
        b = stack[-1]
        stack[0] = b
        stack[-1] = a
    elif instruction in 'ɸ':
        stack.push(len(stack))
    elif instruction in 'β':
        stack.push(stack[stack.pop()])

def STRING(instruction, stack):
    if instruction in 'ɱ':
        a = stack.pop()
        b = stack.pop()
        stack.push(a + b)
    elif instruction in 'f':
        stack.push(len(str(stack.peek())))
    elif instruction in 'v':
        for c in stack.pop():
            stack.push(ord(c))
    elif instruction in 'ʋ':
        a = stack.pop()
        b = stack.pop()
        stack.push(a[b])
    elif instruction in 'ⱱ':
        stack.push(chr(stack.pop()))

def MATH(instruction, stack):
    import math as m
    if instruction in 't':
        stack.push(stack.pop() + stack.pop())
    elif instruction in 'd':
        stack.push(stack.pop() - stack.pop())
    elif instruction in 'θ':
        stack.push(stack.pop() * stack.pop())
    elif instruction in 'ð':
        a = stack.pop()
        b = stack.pop()
        if (b == 0):
            stack.push(0)
        else:
            stack.push(a / b)
    elif instruction in 'n':
        stack.push(stack.pop() % stack.pop())
    elif instruction in 'ʃ':
        stack.push(stack.pop() ** stack.pop())
    elif instruction in 'ʒ':
        stack.push(m.log(stack.pop(), stack.pop()))
    elif instruction in 's':
        stack.push(stack.pop() + stack.pop())
    elif instruction in 'z':
        stack.push(stack.pop() >> stack.pop())
    elif instruction in 'r':
        stack.push(stack.pop() << stack.pop())
    elif instruction in 'ɾ':
        stack.push(stack.pop() & stack.pop())
    elif instruction in 'ɹ':
        stack.push(stack.pop() | stack.pop())
    elif instruction in 'l':
        stack.push(~stack.pop())
    elif instruction in 'ɬ':
        stack.push(-stack.pop())
    elif instruction in 'ɮ':
        stack.push(round(stack.pop()))

def LOGICAL(instruction, stack):
    if instruction in 'ʈ':
        a = stack.pop()
        b = stack.pop()
        if (a == ''):
            stack.push(0)
            return
        if (b == ''):
            stack.push(1)
            return
        if (a > b):
            stack.push(1)
        else:
            stack.push(0)
    elif instruction in 'ɖ':
        a = stack.pop()
        b = stack.pop()
        if (a == ''):
            stack.push(1)
            return
        if (b == ''):
            stack.push(0)
            return
        if (a < b):
            stack.push(0)
        else:
            stack.push(1)
    elif instruction in 'ʂ':
        a = stack.pop()
        b = stack.pop()
        if (a == ''):
            stack.push(0)
            return
        if (b == ''):
            stack.push(1)
            return
        if (a >= b):
            stack.push(1)
        else:
            stack.push(0)
    elif instruction in 'ʐ':
        a = stack.pop()
        b = stack.pop()
        if (a == ''):
            stack.push(1)
            return
        if (b == ''):
            stack.push(0)
            return
        if (a <= b):
            stack.push(0)
        else:
            stack.push(1)
    elif instruction in 'ɳ':
        a = stack.pop()
        b = stack.pop()
        if (a == b):
            stack.push(1)
        else:
            stack.push(0)
    elif instruction in 'ɽ':
        a = stack.pop()
        b = stack.pop()
        if (a == '' or a <= 0):
            a = False
        else:
            a = True
        if (b == '' or b <= 0):
            b = False
        else:
            b = True
        if (a and b):
            stack.push(1)
        else:
            stack.push(0)
    elif instruction in 'ɻ':
        a = stack.pop()
        b = stack.pop()
        if (a == '' or a <= 0):
            a = False
        else:
            a = True
        if (b == '' or b <= 0):
            b = False
        else:
            b = True
        if (a or b):
            stack.push(1)
        else:
            stack.push(0)
    elif instruction in 'ɭ':
        a = stack.pop()
        if (a == '' or a <= 0):
            stack.push(0)
        else:
            stack.push(1)

def IO(instruction, stack):
    if instruction in 'ɪ':
        stack.push(int(input()))
    elif instruction in 'i':
        stack.push(input())
    elif instruction in 'o':
        print(str(stack.pop()))