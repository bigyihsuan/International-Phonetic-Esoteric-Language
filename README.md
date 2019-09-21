# International Phonetic Esoteric Language
WIP

Also known as IPEL. An esoteric, stack-based programming language based around IPA symbols. 100% not associated with the IPA.

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

## Instructions
### Arguments and Returns
Arguments are always taken from the stack via implicit popping. Any instruction can have any number of arguments, which will be noted below.

All instructions return output to the stack. If an instruction has no return value, it does nothing after execution. For instructions that return multiple values, the return values are pushed sequentially (if an instruction returns `a,b`, it will push `a`, then `b`).

### Instructions
#### Literal-related
Character | Returns | Comment
-|-|-
`0-9` | number | `0-9` → `STACK`
`<c>` | string | Push the string into the stack, left to right, as their ASCII/Unicode values

#### Bilabials: Stack Utilities
Bilabials represent various stack utilities.

Character | Arguments | Returns | Comment
-|-|-|-
`p` | `a` | | Pop and discard the top element of the stack.
`b` | | `a` | Copy the top element of the stack.
`ʙ` | | | Swap the top and bottom elements of the stack.
`ɸ` | | number | Pushes the number of elements in the stack.
`β` | number | `a` | Pushes the [number]-th element from the bottom.

#### Labiodentals: String operations
Labiodentals represent various string operations.

Character | Arguments | Returns | Comment
-|-|-|-
`ɱ` | string `a, b` | `ab` | Concatenation.
`f` | string `a`    | number | String length. Will peek at the stack, and return the length of the top element when converted to a string.
`v` | string `a`    | numbers | Converts a string to their numeric value; pushes character by characters.
`ʋ` | string `a`, number `b` | string | Returns the character at that location, 0-indexed.
`ⱱ` | number `a` | string | Converts from a number to a character, based on its ASCII/Unicode value.

#### Dentals, Alveolars, Postalveolars: Mathematics
Dentals, alveolars, and postaveolars represent mathematical instructions. These are always read from left to right. They all return to `STACK`.

Character | Arguments | Returns | Comment
-|-|-|-
`t` | number `a, b` | `a + b` | Addition
`d` | number `a, b` | `a - b` | Subtraction
`θ` | number `a, b` | `a * b` | Multiplication
`ð` | number `a, b` | `a / b` | Division; will return 0 if `b == 0`.
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
`ɮ` | number `a`    | `round(a)` | Rounds `a` to the nearest integer

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
`ɑ ɒ` | Truthy-Jump | On `ɒ`, peek at the stack. If the stack is truthy, jump to the nearest `ɑ`.
`ɘ e` | Falsy-Jump | On `e`, peek at the stack. If the stack is falsy, jump to the nearest `ɘ`.
`ɐ` | Jump | Pop the stack. Jumps to the `a`-th instruction, 0-indexed and `round(a)`-ed. If `a` is a string, will jump to the beginning.
`ɛ ə ɜ` | If-Else | On `ɛ`, peek at the stack. If truthy, execute the code immediately after up to `ə`, then jump to `ɜ`. Otherwise, jump to `ə` and execute to `ɜ`.
`œ ɶ` | Loop | On `œ`, pop `a` from the stack. If truthy, execute the code inside `round(a)` times, jumping from `ɶ` to `œ`. Otherwise, jump to `ɶ`
