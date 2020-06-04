import enums as E
import sys

unvoicedStack = []
voicedStack = []

labels = {} # Maps a str label to an int index in code
tokens = [] # List of tokens.

executionStack = []
state = E.State.BEGIN

stderr = sys.stderr

if (len(sys.argv) == 1):
    # Take code from stdin
    source = sys.stdin
else:
    # Take code from the given file
    source = open(sys.argv[1], "r")

while True:
    c = source.read(1)
    if not c:
        state = E.State.END
        break
    if state == E.State.BEGIN:
        if c == '\n': # ignore newlines
            continue
        if c in '(': # comment
            state = E.State.COMMENT

