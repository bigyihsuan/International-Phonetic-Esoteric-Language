import enums as E
import sys

unvoicedStack = []
voicedStack = []

labels = {} # Maps a str label to an int index in code
state = E.State().BEGIN

if (len(sys.argv) == 1):
    # Take code from stdin
    code = sys.stdin
else:
    # Take code from the given file
    code = open(sys.argv[1], "r")

for line in code.readlines():
    for character in line.strip():
        pass