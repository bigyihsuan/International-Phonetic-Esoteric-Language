# International Phonetic Esoteric Language
WIP
Also known as IPEL. An esoteric, stack-based programming language based around IPA symbols. 100% not associated with the IPA.

## Basic Information
IPEL uses a single stack to store and handle information. All instructions push to the stack after executing.

Types that can go onto this stack are `Numbers` and `Strings`.

Each instruction can have arguments and return values.

## Types
There are 2 types in IPEL: Numbers and Strings.
### Numbers
Numbers are anything numerical. These include integers and floats. Numbers also represent boolean values: 0-like and negative values are falsy, and everything else is truthy.

Number literals are represented in code through square brackets `[]`, or just a single digit. These will push the number literal to the stack.

### Strings
Strings represent both singular characters and strings. They are delimited through angle brackets `<>`. These will also push to the stack.

## Instructions
### Arguments and Returns
All instructions return to the stack. If an instruction has no return value, it does nothing after execution. As a result, code like `!ʘ` will do this:
```python
!  # Wait for user input; then push to the stack
 ʘ # Pop from the stack; print this value
```
For instructions that return multiple values, the first value is put into the register, and all other values are pushed to the stack in reverse order.

Arguments are always taken from the register first, then from the stack via implicit popping. Any instruction can have any number of arguments, which will be noted below.

### Instruction Tables
#### Literal-related
Character | Returns | Comment
-|-|-
`0-9` | number | `0-9` → `STACK`
`[n]` | number | `n` → `STACK`
`c` | string | `c` → `STACK`
`<c>` | string | `c` → `STACK`

#### Bilabials: Stack Operations
Bilabials represent stack operations.

Character | Arguments | Returns | Comment
-|-|-|-
`p` | `a` | - | Pushes `a` onto the stack
`b` | - | `a` | Pops the top off the stack
`m` | - | `a` | Peeks at the top of the stack
`ɸ` | - | number | Checks if the stack is empty; `0, 1` → `STACK`
`β` | - | number | Checks if the register is empty; `0, 1` → `STACK`

#### Labiodentals: String operations
Labiodentals represent various string operations.

Character | Arguments | Returns | Comment
-|-|-|-
`ɱ` | string `a, b` | `ab` | Concatenation
`f` | string `a`    | number | Length
`v` | string `a`    | numbers | Converts a string to their numeric value; pushes character by characters
`ʋ` | string `a`, number `b` | string | Returns the character at that location
`ⱱ` | string `a`, string `b` | number | Returns the index of that character

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
`ʒ` | number `a, b` | `log a (b)` | Logarithm; Base 'a', exponent `b`
`s` | number `a, b` | `a >> b`| Bit shift `a` to the right `b` bits
`z` | number `a, b` | `a << b`| Bit shift `a` to the left `b` bits
`r` | number `a, b` | `a AND b` | Bitwise AND
`ɾ` | number `a, b` | `a OR b` | Bitwise OR
`ɹ` | number `a, b` | `a XOR b` | Bitwise XOR
`l` | number `a`    | `NOT a` | Bitwise NOT (one's complement)
`ɬ` | number `a`    | `-a` | Inverts the sign of `a`.
`ɮ` | number `a`    | `round(a)` | Rounds `a` to the nearest integer

#### Flow Control

#### Clicks: I/O
Character | Arguments | Returns | Comment
-|-|-|-
`!` | | number `a` | Waits for STDIN, then pushes a number to the stack. Will convert any characters to their ASCII values.
`|` || string `a` | Waits for STDIN, then pushes a string to the stack. Digits will be considered as text.
`ʘ` | `a` | | Prints `a` to STDOUT. Prints as strings only (`1a` --> "1a").