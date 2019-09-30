# International Phonetic Esoteric Language
WIP

Also known as IPEL. An esoteric, stack-based programming language based around IPA symbols. 100% not associated with the IPA.

## Running
Clone the repo, navigate to it, and run
```
python3 main.py "code here"
```

## Basic Information
IPEL uses a single stack to store and handle information. All instructions push to the stack after executing.

Types that can go onto this stack are `Numbers` and `Strings`.

Each instruction can have arguments and return values.

Code is read using an instruction pointer iterating through the code left to right. This instruction pointer can jump backwards or forwards though the program based on the instructions read and the stack.

## Types
There are 2 types in IPEL: Numbers and Strings.
### Numbers
Numbers can be integers or floats. Numbers also represent boolean values: 0 and negative values are falsy, and positive values are truthy.

Number literals can only be pushed in a single digit from `0-9`. Additional manipulation will be needed to input larger numbers.

### Strings
Strings are just sequences as characters. These are delimited by `<>`. Strings are always truthy and equal to 1.

## The Stack
The stack holds the two types above and nothing else: numbers and strings. Please note that if an instruction tries to peek or pop at the empty stack will fail and be skipped.

## Instructions
### Arguments and Returns
Arguments are always taken from the stack via implicit popping. Any instruction can have any number of arguments, which will be noted below.

All instructions return output to the stack. If an instruction has no return value, it does nothing after execution. For instructions that return multiple values, the return values are pushed sequentially (if an instruction returns `a,b`, it will push `a`, then `b`).

### Instructions
#### Literal-related
Character | Returns | Comment
-|-|-
`0-9` | number | `0-9` → `STACK`
`<c>` | string | Push the string into the stack.

#### Uvulars: String operations
Uvulars represent various string operations.

Character | Arguments | Returns | Comment
-|-|-|-
`q` | string `a, b` | `ab` | Concatenation.
`ɢ` | string `a`    | number | String length. Will peek at the stack, and return the length of the top element when converted to a string.
`ʀ` | string `a`    | numbers | Converts a string to their numeric value; pushes character by characters.
`ʁ` | string `a`    | strings | Splits a string into its individual characters. Will be pushed into the stack in reverse order (first character on top)
`ɴ` | string `a`, number `b` | string | Returns the character at that location, 0-indexed.
`χ` | number `a` | string | Converts from a number to a character, based on its ASCII/Unicode value.

#### Palatals: Stack Utilities
Palatals represent various stack utilities.

Character | Arguments | Returns | Comment
-|-|-|-
`c` | `a` | | Pop and discard the top element of the stack.
`ɟ` | | `a` | Copy the top element of the stack.
`ɲ` | | | Swap the first and second elements of the stack.
`ç` | | number | Pushes the number of elements in the stack.
`ʝ` | number | `a` | Pushes the `number`-th element from the bottom.
`j` | number | | Rotates the stack `number` elements towards the bottom.
`ʎ` | | | Sorts the stack. Numbers go before strings.

#### Dentals, Alveolars, Postalveolars: Mathematics
Dentals, alveolars, and postaveolars represent mathematical instructions. These are always read from left to right. They all return to `STACK`.

Character | Arguments | Returns | Comment
-|-|-|-
`t` | number `a, b` | `a + b` | Addition
`d` | number `a, b` | `a - b` | Subtraction
`θ` | number `a, b` | `a * b` | Multiplication
`ð` | number `a, b` | `a / b` | Division; will return 0 if `b == 0`. If `a` and `b` are `int`s, will perform `a // b`.
`n` | number `a, b` | `a % b` | Modulo
`ʃ` | number `a, b` | `a ^ b` | Exponent; Base `a`, exponent `b`
`ʒ` | number `a, b` | `log a (b)` | Logarithm; Base `a`, exponent `b`
`s` | number `a, b` | `a >> b`| Bit shift `a` to the right `b` bits
`z` | number `a, b` | `a << b`| Bit shift `a` to the left `b` bits
`r` | number `a, b` | `a AND b` | Bitwise AND
`ɾ` | number `a, b` | `a OR b` | Bitwise OR
`ɹ` | number `a, b` | `a XOR b` | Bitwise XOR
`l` | number `a`    | `NOT a` | Bitwise NOT
`ɬ` | number `a`    | `-a` | Inverts the sign of `a`.
`ɮ` | number `a`    | `ceil(a)` | Rounds `a` to the largest integer

#### Retroflexes: Comparisons and Logical Operators
Retroflex consonants represent comparisons. They (almost) always take 2 arguments. For all instructions, ASCII order is used for strings. Empty strings are always last.

Character | Arguments | Returns | Comment
-|-|-|-
`ʈ` | `a, b` | `a > b` | Returns 1 if true, 0 if false.
`ɖ` | `a, b` | `a < b` | Returns 1 if true, 0 if false.
`ʂ` | `a, b` | `a >= b` | Returns 1 if true, 0 if false.
`ʐ` | `a, b` | `a <= b` | Returns 1 if true, 0 if false.
`ɳ` | `a, b` | `a == b` | Returns 1 if true, 0 if false.
`ɽ` | `a, b` | `a and b` | Logical AND. Returns 1 if both arguments are truthy, 0 otherwise.
`ɻ` | `a, b` | `a or b` | Logical OR. Returns 1 if either argument is truthy, 0 otherwise.
`ɭ` | `a` | `not a` | Logical NOT. Returns 1 if the argument is falsy, 0 otherwise.


#### I/O
Character | Arguments | Returns | Comment
-|-|-|-
`ɪ` | | number `a` | Waits for STDIN, then pushes a number to the stack. Will convert any characters to their ASCII/Unicode values.
`i` | | string `a` | Waits for STDIN, then pushes the string to the stack.
`o` | `a` | | Prints `a` to STDOUT. Prints a string.

#### Control Flow
Some vowels are used as flow control. Certain pairs of vowels are used as delimiters for the flow control structures.

Character | Structure | Comment
-|-|-
`ɑ ɒ` | Truthy-Jump | On `ɒ`, pop the stack. If the stack is truthy, jump to the nearest `ɑ`.
`ɘ e` | Falsy-Jump | On `e`, pop the stack. If the stack is falsy, jump to the nearest `ɘ`.
`ɐ` | Jump | Pop the stack. Jumps to the `a`-th instruction, 0-indexed and `ceil(a)`-ed. If `a` is a string, will jump to the beginning.
`ɛ ə ɜ` | If-Else | On `ɛ`, pop the stack. If truthy, execute the code immediately after up to `ə`, then jump to `ɜ`. Otherwise, jump to `ə` and execute to `ɜ` and continue.
`œ ɶ` | Loop | On `œ`, pop `a` from the stack. If truthy and a number, execute the code inside `ceil(a)` times, jumping from `ɶ` to `œ`. Otherwise, jump to `ɶ`
