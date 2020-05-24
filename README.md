# International Phonetic Esoteric Language
WIP

Also known as IPEL. An esoteric, stack-based programming language based around IPA symbols. 100% not associated with the IPA.

## Running
TODO

## Basic Information
IPEL uses three stacks: two value stacks, and an execution stack. The value stacks are read-writable. The execution stack is used internally to handle execution of code; it is read-only.

Code is run by pushing values into the value stack and instructions into the instruction stack. See below for the types of IPEL.

## The Value Stacks
The value stack holds the two types above and nothing else: numbers and strings. Please note that if an instruction tries to peek or pop an empty value stack, it will `nop` and be skipped.

There are two value stacks: the `Unvoiced` stack (U stack) and the `Voiced` stack (V stack). By default, values are pushed onto the U stack.

### Voice Switching
To change the stack that values are pushed onto, `U` and `V` are used as voicing flags, changing the voicing to `Unvoiced` and `Voiced` respectively. This continues until the interpreter encounters another voicing flag, or the end of the program.

## The Execution Stack
The execution stack (E stack) stores the location in the code to return to after executing a function. When a function is called, the location of the instruction following it is pushed into the E stack. When the function returns, the interpreter pops the E stack and jumps back to the location popped.

## Comments
Comments are non-whitespace characters surrounded by parentheses `(like this)`.

Comments end when a closing parenthesis `)` appears.

```
(this is a comment)
(This is a comment (not nested)
(comment with
    (a newline and tab)
```

## Types
There are 3 types in IPEL: Numbers, Strings, and Lists.

### Numbers
A number is any real number. Numbers also represent boolean values: 0 and negative values are falsy, and positive values are truthy.

Integers can be pushed in as a single decimal digit from `0-9`, or any number of decimal digits within square brackets `{12345}`.

Floats can be pushed in using the multidigit notation: `{123.456}`. A number in the form `{d.}` where `d` is a digit is invalid.

```
7 ( -- 7)
78 ( -- 7 8)
{123} ( -- 123)
{1.23} ( -- 1.23)
1{3.3}0 ( -- 1 3.3 0)
{3.5} ( -- 3.5)
```

### Lists
Lists are data structures in IPEL that can hold any number of elements of any type. Lists are not limited to a single type; they can hold any and all of the three types.

Lists are created by surrounding its elements with square brackets `[elements]`. List elements are separated using periods `.`: `[a.b.c]`.

Nested lists are denoted by a list within a list: `[[nest].ele.[nest]]`. Periods preceding the first element and following the last element are optional.

Non-empty lists are considered truthy.

```
[] (empty list)
[1.2.3]
[{1.2}."string".3] (note that internally "string" is a list)
[["nested"].["list".["in list"]]."it is"]
```

### Strings
Strings are lists of integers with length 0 or greater. These are delimited by `"`.

Non-empty strings, like lists, are considered truthy.

All instructions that work on lists also work on strings.

#### Escape Sequences
`\` preceding certain characters will escape it according to the [Python escape sequences](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals).

```
Examples (before -- after)
-------------------------
"abc" ( -- "abc")
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


#### Literals
| Character  | Type   | Comment                                                      |
| ---------- | ------ | ------------------------------------------------------------ |
| `0-9`      | number | Pushes the decimal number literal.                           |
| `{NUMBER}` | number | Pushes the decimal number literal within the square brackets. |
| `[a.b.c]`  | list   | Push the given list with period-separated elements           |
| `"STRING"` | list   | Push the string as a list of numbers into the stack.         |

#### Voicings
| Character | Stack Effect    | Comment                                                      |
| --------- | --------------- | ------------------------------------------------------------ |
| `ɸ`       | -               | Sets the voicing to `Unvoiced`.                              |
| `β`       | -               | Sets the voicing to `Voiced`.                                |
| `ɓ`       | `( -- voicing)` | Pushes the current voicing. `0` for unvoiced, `1` for voiced. |


#### Plosives/Stops: Stack Operations
Plosives modify the stack.

| Instruction | Stack Effect           | Comment                                                      |
| ----------- | ---------------------- | ------------------------------------------------------------ |
| `p`         | `(a -- )`              | Pop and discard the top element of the stack.                |
| `b`         | `(a -- a a)`           | Duplicate the top element of the stack.                      |
| `t`         | `( -- size)`           | Push the size of the stack.                                  |
| `d`         | `(a b -- b a)`         | Swap the first and second elements of the stack.             |
| `ʈ`         | `(c b a -- a c b)`     | Rotate the top 3 elements clockwise (upwards).               |
| `ɖ`         | `(c b a -- b a c)`     | Rotate the top 3 elements counterclockwise (downwards).      |
| `c`         | `(d b a c -- d c b a)` | Sort the stack. Numbers go before strings. Lower values on top. |
| `k`         | `A(a -- ) B( -- a)`    | Pop the top of the current stack and push it onto the other one. |
| `g`         | `A( -- a) B(a -- )`    | Pop the top of the other stack and push it onto the current one. |

#### Central Vowels: Comparisons and Logical Operators
Approximates and laterals represent comparisons. For all instructions, `1` is pushed if true, and `0` if false.

ASCII/Unicode order is used for strings. Empty strings are first, followed by shorter stings.

| Character | Stack Effect    | Comment                  |
| --------- | --------------- | ------------------------ |
| `ɨ`       | `(a b -- a>b)`  | Greater than             |
| `ʉ`       | `(a b -- a>=b)` | Greater than or equal to |
| `ə`       | `(a b -- a==b)` | Equal to                 |
| `ɘ`       | `(a b -- a<b)`  | Less than                |
| `ɵ`       | `(a b -- a<=b)` | Less than or equal to    |
| `ɜ`       | `(a b -- a&&b)` | Logical AND              |
| `ɞ`       | `(a b -- a||b)` | Logical OR               |
| `ɐ`       | `(a -- !a)`     | Logical NOT              |

#### Frontal Fricatives, Taps/Flaps, Trills: Mathematics
Fricatives, taps, flaps, and trills represent mathematical instructions.

| Character | Stack Effect         | Comment                                                      |
| --------- | -------------------- | ------------------------------------------------------------ |
| `s`       | `(a b -- a+b)`       | Addition                                                     |
| `z`       | `(a b -- a-b)`       | Subtraction                                                  |
| `f`       | `(a b -- a*b)`       | Multiplication                                               |
| `v`       | `(a b -- a/b)`       | Division; will return 0 if `b == 0`. If `a` and `b` are integers, will perform `a // b`. |
| `ⱱ`       | `(a b -- a%b)`       | Modulo (Labiodental Tap ⱱ)                                   |
| `ʃ`       | `(a b -- a**b)`      | Exponent; Base `a`, exponent `b`                             |
| `ʒ`       | `(a b -- log(a, b))` | Logarithm; Base `a`, exponent `b`                            |
| `θ`       | `(a b -- a>>b)`      | Bit shift `a` to the right `b` bits                          |
| `ð`       | `(a b -- a<<b)`      | Bit shift `a` to the left `b` bits                           |
| `ʂ`       | `(a b -- a&b)`       | Bitwise AND                                                  |
| `ʐ`       | `(a b -- a|b)`       | Bitwise OR                                                   |
| `r`       | `(a -- !a)`          | Bitwise NOT                                                  |
| `ɾ`       | `(a -- -a)`          | Inverts the sign of `a`.                                     |
| `ɽ`       | `(a -- ceil(a))`     | Rounds `a` to the largest integer                            |
| `ɬ`       | `(a b -- max)`       | Minimum                                                      |
| `ɮ`       | `(a b -- min)`       | Maximum                                                      |

#### Back Fricatives, Taps/Flaps, Trills: List and String operations
Back fricatives, taps, flaps, and trills represent operations on lists. String operations are also in this section.

| Character | Stack Effect          | Comment                                                      |
| --------- | --------------------- | ------------------------------------------------------------ |
| `x`       | `(abc def -- abcdef)` | Concatenation.                                               |
| `ɣ`       | `(a ... z n -- list)` | Concatenates the next `n` elements popped off the stack into a list of length `n`. |
| `ħ`       | `(a -- a n)`          | List length. Pushes the length of the element popped.        |
| `ʀ`       | `(list -- a b ...)`   | Splits a list into its individual elements.                  |
| `h`       | `(list n -- list e)`  | Returns the element `e` at `n`, 0-indexed.                   |
| `χ`       | `(num -- str)`        | Converts a number to a single-character string, based on its ASCII/Unicode value. |
| `ʁ`       | `(str -- s t r)`      | Converts a string to its ASCII/Unicode value.                |

#### Vowels: I/O

I/O is handled by a set of close-to-mid front and back vowels. Front vowels handle input from STDIN, and back vowels handle output to STDOUT.

| Character | Stack Effect        | Comment                                                      |
| --------- | ------------------- | ------------------------------------------------------------ |
| `i`       | `( -- str)`         | Pushes a line from STDIN.                                    |
| `y`       | `( -- str str str)` | Pushes a line from STDIN, separating by whitespace.          |
| `ɪ`       | `( -- int)`         | Pushes an integer from STDIN. Silently `nop`s when it cannot find an integer. |
| `ʏ`       | `( -- float)`       | Pushes a float from STDIN. Silently `nop`s when it cannot find a float. |
| `o`       | `(ele trail -- )`   | Pops and outputs to STDIN with the trailing element `trail`. |

## Functions

Functions are not actually true "functions", per se, since they do not take input, and are more like procedures since they act directly on the stack. They are most analogous to Forth definitions in declaration and use.

Functions must be declared before they are called. If not, the interpreter will ignore it.

Functions are declared and called as the following, whitespace omitted:
```
<name>/code/
<name>
```
Function `name`s are strings of any non-whitespace characters that are not `<>/` and start with a non-numeric character.  They are also case sensitive.

Functions can be overwritten by declaring them again with `<name>/new code/`.

Functions cannot be declared in a function, but they can be called in a function declaration for recursion, like `<name>/some code <name> more code/`.

## Control Structures

Control structures in IPEL change where the instruction pointer goes next.


| Character  | Stack Effect | Comment                                                      |
| ---------- | ------------ | ------------------------------------------------------------ |
| `ʌ`        | `(con -- )`  | Conditional Skip: If `con` is truthy, skip the next instruction. |
| `ʎ❬label❭` | `( -- )`     | Label: Signifies a label at the location of `ʎ❬label❭` with the name `str`. |
| `ʟ❬label❭` | `( -- )`     | Go-To Label: Jumps execution to the instruction after `ʎ❬label❭`. |

### Conditional Skip

The Conditional Skip pops the currently voiced stack for a value `con`. If `con` is truthy, the next instruction will be skipped.

### Labels and Go-To Label

The instructions `ʎ` and `ʟ` use the special syntax `❬label❭` following them to define arbitrary locations in the code to jump to.

Labels are delimited by angle brackets `❬label❭`. Labels can have any string within the brackets, stopping at the first `❭`.

`ʎ` before a label creates a label at that location. `ʟ` before a label will unconditionally jump execution to the instruction following given label.

Conditional jumps can be created using a combination of comparison/logical operators, conditional skip, and labels.