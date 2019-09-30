# coding=UTF-8

def LITERAL(instruction, stack):
    if (str.isdigit(instruction)):
        stack.push(int(instruction))
    else:
        stack.push(instruction)


def STRING(instruction, stack):
    if not stack.isEmpty():
        if instruction in 'q' and stack.size() >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.push(a + b)
        elif instruction in 'ɢ':
            stack.push(len(str(stack.peek())))
        elif instruction in 'ʀ':
            for c in stack.pop():
                stack.push(ord(c))
        elif instruction in 'ʁ':
            a = str(stack.pop())[::-1]
            for c in a:
                stack.push(c)
        elif instruction in 'ɴ' and stack.size() >= 2:
            a = stack.pop()
            b = stack.pop()
            stack.push(a[b])
        elif instruction in 'χ':
            stack.push(chr(stack.pop()))

def STACK(instruction, stack):
    if not stack.isEmpty():
        if instruction in 'c':
            stack.pop()
        elif instruction in 'ɟ':
            if not stack.isEmpty():
                stack.push(stack.peek())
            elif instruction in 'ɲ' and stack.size() >= 2:
                a = stack.stack[0]
                b = stack.stack[1]
                stack.stack[0] = b
                stack.stack[1] = a
            elif instruction in 'ç':
                stack.push(stack.size())
            elif instruction in 'ʝ':
                stack.push(stack.stack[stack.pop()])
            elif instruction in 'j':
                a = stack.pop()
                for i in range(a, 0, -1):
                    stack.push(stack.stack.pop(0))
            elif instruction in 'ʎ':
                ints, strs = [], []
                while not stack.isEmpty():
                    ele = stack.pop()
                    if isinstance(ele, int):
                        ints.append(ele)
                    else:
                        strs.append(ele)
                        ints.sort()
                        strs.sort()
                        ints.extend(strs)
                        for i in ints:
                            stack.push(i)
                            stack.stack.reverse()

def MATH(instruction, stack):
    import math as m
    if not stack.isEmpty():
        if stack.size() >= 2:
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
        else:
            if instruction in 'l':
            stack.push(~stack.pop())
            elif instruction in 'ɬ':
                stack.push(-stack.pop())
            elif instruction in 'ɮ':
                stack.push(round(stack.pop()))

def LOGICAL(instruction, stack):
    if not stack.isEmpty():
        if stack.size() >= 2:
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
        temp = input()
        if temp.isnumeric():
            stack.push(int(temp))
        elif temp[0] == '-' and temp[1:].isnumeric():
            stack.push(int(temp))
        else:
            for c in temp:
                stack.push(ord(c))
    elif instruction in 'i':
        stack.push(input())
    elif instruction in 'o' and not stack.isEmpty():
        print(str(stack.pop()))
