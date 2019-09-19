import sys
import string
import stack as s

codePath = sys.argv[1] if (sys.argv[1] != None) else sys.argv[0] # python.exe .\main.py [code path]
codeFile = open(codePath, 'r', encoding="UTF-8")
code = ""
dataStack = s.Stack()

