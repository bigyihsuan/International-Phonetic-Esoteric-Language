# International Phonetic Esoteric Language
WIP

Also known as IPEL. An esoteric, stack-based programming language based around IPA symbols. 100% not associated with the IPA.

## Running
TODO

## Basic Information
IPEL uses three stacks: two value stacks, and an execution stack. The value stacks are read-writable. The execution stack is used internally to handle execution of code; it is read-only.

Code is run by pushing values into the value stack and instructions into the instruction stack. See below for the types of IPEL.

## The Value Stacks
The value stack holds the two types above and nothing else: numbers and strings. Please note that if an instruction tries to peek or pop an empty value stack, it will nop and be skipped.

There are two value stacks: the `Unvoiced` stack (U stack) and the `Voiced` stack (V stack). By default, values are pushed onto the U stack.

### Voice Switching
To change the stack that values are pushed onto, `U` and `V` are used as voicing flags, changing the voicing to `Unvoiced` and `Voiced` respectively. This continues until the interpreter encounters another voicing flag, or the end of the program.

## The Execution Stack
The execution stack (E stack) stores the location in the code to return to after executing a function. When a function is called, the location of the instruction following it is pushed into the E stack. When the function returns, the interpreter pops the E stack and jumps back to the location popped.

## Types
There are 2 types in IPEL: Numbers and Strings.

### Numbers
A number is any real number. Numbers also represent boolean values: 0 and negative values are falsy, and positive values are truthy.

Integers can be pushed in as a single decimal digit from `0-9`, or any number of decimal digits within square brackets `[12345]`.

Floats can be pushed in using the multidigit notation: `[123.456]`. Note this means the value `1f` will need to be pushed in as `[1.0]`.

```
Example (before -- after)
-------------------------
7 ( -- 7)
78 ( -- 7 8)
[1.23] ( -- 1.23)
1[3.3]0 ( -- 1 3.3 0)
[3.5] ( -- 3.5)
```

### Strings
Strings are sequences of characters with length 0 or greater. These are delimited by `"`. Strings are always truthy and equal to 1 when converted to a number.

#### Escape Sequences
`\` preceding certain characters will escape it according to the [Python escape sequences](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals).

```
Example (before -- after)
-------------------------
"abc" ( -- "abc" )
"a""b""c" ( -- "a" "b" "c")
"" ( -- "" )
"a \
b" ( -- "a b")
"\n" ( -- "\n")
"\"<>" ( -- "\"<>")
"'hello'" (-- "'hello'")
```


## Instructions
Instructions are denoted as letters in the [International Phonetic Alphabet](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) (IPA).

The stack that an instruction works on is dependent on the current voicing.

#### Comments
Comments are characters surrounded by parentheses `(like this)`.

Comments end when a closing parenthesis `)` appears.

```
(this is a comment)
(This is a comment (not nested comment)
(comment with
    a newline and tab)
```

#### Literal-Related
Character | Pushes | Comment
-|-|-
`0-9` | number | Pushes the decimal number literal.
`[NUMBER]` | number | Pushes the decimal number literal within the square brackets.
`"STRING"` | string | Push the string into the stack.
`U` | - | Sets the voicing to `Unvoiced`.
`V` | - | Sets the voicing to `Voiced`.


#### Plosives/Stops: Stack Utilities
Plosives modify the stack.

Instruction | Stack Effect | Comment
-|-|-
`p` | `(a -- )` | Pop and discard the top element of the stack.
`b` | `(a -- a a)` | Push the top element of the stack.
`t` | `( -- a)` | Push the number of elements in the stack.
`d` | `(a -- b)` | Push the `a`-th element from the bottom.
`ʈ` | `(a b -- b a)` | Swap the first and second elements of the stack.
`ɖ` | `(a -- )` | Rotate the stack `a` times towards the bottom.
`c` | `(d b a c -- d c b a)` | Sort the stack. Numbers go before strings. Lower values on top.
`k` | `A(a -- ) B( -- a)`  |  Pop the top of the current stack and push it onto the other one.
`g` | `A( -- a) B(a -- )`  |  Pop the top of the other stack and push it onto the current one.

#### Approximates and Laterals: Comparisons and Logical Operators
Approximates and laterals represent comparisons. For all instructions, `1` is pushed if true, and `0` if false.

ASCII/Unicode order is used for strings. Empty strings are first, followed by shorter stings.

Character | Stack Effect | Comment
-|-|-
`ɹ` | `(b a -- a>b )` | Greater than
`ɻ` | `(b a -- a>=b )` | Greater than or equal to
`l` | `(b a -- a<b )` | Less than
`ɭ` | `(b a -- a<=b )` | Less than or equal to
`ʋ` | `(b a -- a==b )` | Equal to
`ł` | `(b a -- a&&b )` | Logical AND
`ɮ` | `(b a -- a||b )` | Logical OR
`ʎ` | `(b a -- a^^b)` | Logical XOR
`ʟ` | `(a -- !a)` | Logical NOT

#### Frontal Fricatives, Taps/Flaps, Trills: Mathematics
Fricatives, taps, flaps, and trills represent mathematical instructions.

Character | Stack Effect | Comment
-|-|-
`s` | `(b a -- a+b)` | Addition
`z` | `(b a -- a-b)` | Subtraction
`f` | `(b a -- a*b)` | Multiplication
`v` | `(b a -- a/b)` | Division; will return 0 if `b == 0`. If `a` and `b` are integers, will perform `a // b`.
`ⱱ` | `(b a -- a%b)` | Modulo (Labiodental Tap ⱱ)
`ʃ` | `(b a -- a**b)` | Exponent; Base `a`, exponent `b`
`ʒ` | `(b a -- log(a, b)` | Logarithm; Base `a`, exponent `b`
`θ` | `(b a -- a>>b)` | Bit shift `a` to the right `b` bits
`ð` | `(b a -- a<<b)` | Bit shift `a` to the left `b` bits
`ʂ` | `(b a -- a&b)` | Bitwise AND
`ʐ` | `(b a -- a|b)` | Bitwise OR
`ɕ` | `(b a -- a^b)` | Bitwise XOR
`r` | `(a -- !a)` | Bitwise NOT
`ɾ` | `(a -- -a)` | Inverts the sign of `a`.
`ɽ` | `(a -- ceil(a))` | Rounds `a` to the largest integer

#### Back Fricatives, Taps/Flaps, Trills: String operations
Back fricatives, taps, flaps, and trills represent instructions that handle strings.

Character | Stack Effect | Comment
-|-|-
`x` | `(def abc -- abcdef)` | Concatenation.
`ɣ` | `(a -- a n)` | String length. Will peek at the stack, and return the length of the top element when converted to a string.
`χ` | `(a -- c)` | Converts a number to a character, based on its ASCII/Unicode value.
`ʁ` | `(abc -- p o n)` | Converts a string to its ASCII/Unicode value. Will push character by character in reverse order.
`ʀ` | `(abc -- c b a)` | Splits a string into its individual characters. Will be pushed into the stack in reverse order.
`h` | `(abc n -- o)` | Returns the character at `n`, 0-indexed.

#### I/O
Character | Arguments | Returns | Comment
-|-|-|-
`ɪ` | | number `a` | Waits for STDIN, then pushes a number to the stack. Will convert any characters to their ASCII/Unicode values.
`i` | | string `a` | Waits for STDIN, then pushes the string to the stack.
`o` | `a` | | Prints `a` to STDOUT as a string with trailing newline.

#### Vowels: Control Flow
Some vowels are used as flow control. Certain pairs of vowels are used as delimiters for the flow control structures.

Character | Structure | Comment
-|-|-
`ɑ ɒ` | Truthy-Jump | On `ɒ`, pop the stack. If the stack is truthy, jump to the nearest `ɑ`.
`ɘ e` | Falsy-Jump | On `e`, pop the stack. If the stack is falsy, jump to the nearest `ɘ`.
`ɐ` | Jump | Pop the stack. Jumps to the `a`-th instruction, 0-indexed and `ceil(a)`-ed. If `a` is a string, will jump to the beginning.
`ɛ ə ɜ` | If-Else | On `ɛ`, pop the stack. If truthy, execute the code immediately after up to `ə`, then jump to `ɜ`. Otherwise, jump to `ə` and execute to `ɜ` and continue.
`æ œ` | For Loop | On `æ`, pop `a`. If `a` is a number and `a >= 0`, the code between `æ` and `œ` will be executed `ceil(a)` times.

#### Glottals: Functions
Functions are not actually true "functions", per se, since they do not take input, and are more like procedures since they act directly on the stack.

Functions must be declared before they are called. If not, the interpreter will ignore it.

Functions are declared and called as the following, whitespace omitted:
```
ʢ name ʡʕ code ʔ
{ name }
```
`name` can contain any non-whitespace character. Anything located between `ʡʕ` is ignored.

Functions can be declared in functions and can be called outside of the function it is declared in (all functions are global).