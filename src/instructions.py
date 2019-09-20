def LITERAL(instruction, stack):
    if (str.isdigit(instruction)):
        stack.push(int(instruction))
    else:
        stack.push(instruction)

def STRING(instruction, stack):
    if instruction in 'ɱ':
        a = stack.pop()
        b = stack.pop()
        stack.push(a + b)
    else if instruction in 'f':
        stack.push(len(str(stack.peek())))
    else if instruction in 'v':
        for c in stack.pop():
            stack.push(ord(c))
    else if instruction in `ʋ`:
        a = stack.pop()
        b = stack.pop()
        stack.push(a[b])
    else if instruction in 'ⱱ':
        stack.push(chr(stack.pop()))

def MATH(instruction, stack):
    import math as m
    if instruction in 't':
        stack.push(stack.pop() + stack.pop())
    else if instruction in 'd':
        stack.push(stack.pop() - stack.pop())
    else if instruction in 'θ':
        stack.push(stack.pop() * stack.pop())
    else if instruction in 'ð':
        a = stack.pop()
        b = stack.pop()
        if (b == 0):
            stack.push(0)
        else:
            stack.push(a / b)
    else if instruction in 'n':
        stack.push(stack.pop() % stack.pop())
    else if instruction in 'ʃ':
        stack.push(stack.pop() ** stack.pop())
    else if instruction in 'ʒ':
        stack.push(m.log(stack.pop(), stack.pop()))
    else if instruction in 's':
        stack.push(stack.pop() + stack.pop())
    else if instruction in 'z':
        stack.push(stack.pop() >> stack.pop())
    else if instruction in 'r':
        stack.push(stack.pop() << stack.pop())
    else if instruction in 'ɾ':
        stack.push(stack.pop() & stack.pop())
    else if instruction in 'ɹ':
        stack.push(stack.pop() | stack.pop())
    else if instruction in 'l':
        stack.push(~stack.pop())
    else if instruction in 'ɬ':
        stack.push(-stack.pop())
    else if instruction in 'ɮ':
        stack.push(round(stack.pop()))

def IO(instruction, stack):
    if instruction in 'ɪ':
        for c in input():
            stack.push(ord(a))
    else if instruction in 'i':
        stack.push(input())
    else if instruction in 'o':
        print(stack.pop())