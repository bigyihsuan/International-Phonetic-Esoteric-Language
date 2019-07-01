class Stack:
    def __init__(self):
        self.stack = []

    def push(self, ele):
        if (type(ele) == "<class 'str'>"):
            for c in ele:
                self.stack.append(ord(ele))
        else:
            self.stack.append(ele)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]

    def isEmpty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)