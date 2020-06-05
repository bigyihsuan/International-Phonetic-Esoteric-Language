import enums as E
import sys

unvoicedStack = []
voicedStack = []

labels = {} # Maps a  label to a location in code.
            # Also maps the name of a function to its location.
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

