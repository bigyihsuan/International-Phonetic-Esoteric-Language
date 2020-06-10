# International Phonetic Esoteric Language

## What is this?

The International Phonetic Esoteric Language (IPEL) is a personal project of mine to create a simple, stack-based esoteric programming language from scratch to challenge myself. I also decided to base its instruction set on the International Phonetic Alphabet by the International Phonetic Association, modeling the appearance of a typical phonetic transcription, such as `/hε.lɔ.wɔɹld/` for a rough approximation of "hello world".

It is meant for code golf, and is definitely not made for any sort of serious use.

## Installation

Install this by cloning this repository (`https://github.com/bigyihsuan/International-Phonetic-Esoteric-Language`).

## Execution

Execute the IPEL code by navigating to the repository folder and running `interpreter.py` with Python 3.

```
$ python3 interpreter.py [options] codeFile
```

`codeFile` is any file that contains IPEL code.

`[options]` is one of the following:

* `-d`: Runs the interpreter in debug mode. The interpreter will print the label mappings and the parsed lexemes. It will also print the data and execution stacks after every instruction.

## Basic Information
IPEL uses three stacks: two value stacks, and an execution stack. The value stacks are read-writable. The execution stack is used internally to handle function execution; it is read-only.

Code is run by pushing values into the value stack and instructions into the instruction stack. See below for the types of IPEL.

## The Value Stacks
The value stack holds the two types above and nothing else: numbers and strings. Please note that if an instruction tries to peek or pop an empty value stack, it will `nop` and be skipped.

There are two value stacks: the `Unvoiced` stack (U stack) and the `Voiced` stack (V stack). By default, values are pushed onto the U stack.

### Voice Switching
To change the stack that values are pushed onto, `ɸ` and `β` are used as voicing flags, changing the voicing to `Unvoiced` and `Voiced` respectively. This continues until the interpreter encounters another voicing flag, or the end of the program.

## The Execution Stack
The execution stack stores the location in the code to return to after executing a function. When a function is called, the location of the instruction following it is pushed into the E stack. When the function returns, the interpreter pops the E stack and jumps back to the location popped.

## Comments
Comments are characters surrounded by parentheses `(like this)`.

Comments end when a closing parenthesis `)` appears.

```
(this is a comment)
(This is a comment (not nested)
(comment with
    (a newline and tab)
```

A helpful comment is the stack effect diagram, which notes the stack before and after an operation.

```
(before -- after)
(bottom top -- bottom top)
```

The top of the stack is to the right.

## Types
There are 3 types in IPEL: Numbers, Strings, and Lists.

### Numbers
A number is any real number. Numbers also represent boolean values: 0 is falsy, and non-0 values are truthy.

Integers can be pushed in as a single decimal digit from `0-9`, or any number of decimal digits within square brackets `{12345}`.

Floats can be pushed in using the multidigit notation: `{123.456}`. A number in the form `{d.}` where `d` is a digit is invalid. This is the same with the form `{.d}`.

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

Nested lists are denoted by a list within a list: `[[nest].ele.[nest]]`. Periods following the last element are optional.

Empty lists are falsy, and are otherwise truthy.

```
[] (empty list)
[1.2.3]
[{1.2}."string".3]
[["nested"].["list".["in list"]]."it is"]
```

### Strings
Strings are sequences of characters. These are delimited by `"`.

Like lists, empty strings are falsy and are otherwise truthy.

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
| `c`         | `(d b a c -- d c b a)` | Sort the stack. Numbers before Strings before Lists. Order of lists in the stack is preserved. Lower values on top. |
| `k`         | `A(a -- ) B( -- a)`    | Pop the top of the current stack and push it onto the other one. |
| `g`         | `A( -- a) B(a -- )`    | Pop the top of the other stack and push it onto the current one. |

#### Central Vowels: Comparisons and Logical Operators
Approximates and laterals represent comparisons. For all instructions, `1` is pushed if true, and `0` if false.

ASCII/Unicode order is used for strings. Empty strings are first, followed by shorter stings.

Comparing lists does not work except for the `ə` "Equal to" operator, where it will check for equality. The interpreter will NOP the instruction if it isn't the case

| Character | Stack Effect    | Comment                  |
| --------- | --------------- | ------------------------ |
| `ɨ`       | `(a b -- a>b)`  | Greater than             |
| `ʉ`       | `(a b -- a>=b)` | Greater than or equal to |
| `ə`       | `(a b -- a==b)` | Equal to                 |
| `ɘ`       | `(a b -- a<b)`  | Less than                |
| `ɵ`       | `(a b -- a<=b)` | Less than or equal to    |
| `ɜ`       | `(a b -- a and b)` | Logical AND              |
| `ɞ`       | `(a b -- a or b)` | Logical OR               |
| `ɐ`       | `(a -- not a)`     | Logical NOT              |

#### Frontal Fricatives, Taps/Flaps, Trills: Mathematics
Fricatives, taps, flaps, and trills represent mathematical instructions.

These only apply to numbers. Otherwise, the interpreter will NOP the instruction.

| Character | Stack Effect         | Comment                                                      |
| --------- | -------------------- | ------------------------------------------------------------ |
| `s`       | `(a b -- a+b)`       | Addition |
| `z`       | `(a b -- a-b)`       | Subtraction |
| `f`       | `(a b -- a*b)`       | Multiplication  |
| `v`       | `(a b -- a/b)`       | Division; will return 0 if `b == 0`. If `a` and `b` are integers, will perform `a // b`. |
| `ⱱ`       | `(a b -- a%b)`       | Modulo (Labiodental Tap ⱱ)                                   |
| `ʃ`       | `(a b -- a**b)`      | Exponent; Base `a`, exponent `b`                             |
| `ʒ`       | `(a b -- log(a, b))` | Logarithm; Base `a`, exponent `b`                            |
| `θ`       | `(a b -- a>>b)`      | Bit shift `a` to the right `b` bits                          |
| `ð`       | `(a b -- a<<b)`      | Bit shift `a` to the left `b` bits                           |
| `ʂ`       | `(a b -- a&b)`       | Bitwise AND                                                  |
| `ʐ`       | `(a b -- a\|b)`       | Bitwise OR                                                   |
| `r`       | `(a -- !a)`          | Bitwise NOT                                                  |
| `ɾ`       | `(a -- -a)`          | Inverts the sign of `a`.                                     |
| `ɽ`       | `(a -- ceil(a))`     | Rounds `a` to the largest integer                            |
| `ʙ`       | `(a -- floor(a))`     | Rounds `a` to the smallest integer                            |
| `ɬ`       | `(a b -- max)`       | Minimum                                                      |
| `ɮ`       | `(a b -- min)`       | Maximum                                                      |

#### Back Fricatives, Taps/Flaps, Trills: List and String operations
Back fricatives, taps, flaps, and trills represent operations on lists. String operations are also in this section.

| Character | Stack Effect          | Comment                                                      |
| --------- | --------------------- | ------------------------------------------------------------ |
| `x`       | `(abc def -- abcdef)` | Concatenation. Implicitly casts its arguments into strings, then lists if they are not lists. |
| `ɣ`       | `(a ... z n -- list)` | Concatenates the next `n` elements popped off the stack into a list of length `n`. Will NOP if `n` is not a number and does `ceil(n)` if it is. |
| `ħ`       | `(a -- a n)`          | List length. Pushes the length of the element peeked. Casts `a` to a list to get its length. `a`'s type is retained. |
| `ʀ`       | `(list -- a b ...)`   | Splits a list into its individual elements. Implicitly casts `list` to a list. |
| `h`       | `(list n -- list e)`  | Returns the element `e` at `n`, 0-indexed. Will NOP if `n` is not a number and does `ceil(n)` if it is |
| `χ`       | `(num -- str)`        | Converts a number to a single-character string, based on its ASCII/Unicode value. Will NOP if `num` is not a number, and `ceil(num)` if it is. |
| `ʁ`       | `(str -- s t r)`      | Converts a string to a list of integers representing their `ord()` values. Will NOP if `str` is not a list of single-character strings or a string. |
| `ʕ`       | `(list -- str)`      | Converts a list to a string. |

#### Vowels: I/O

I/O is handled by a set of close-to-mid front and back vowels. Front vowels handle input from STDIN, and back vowels handle output to STDOUT.

| Character | Stack Effect        | Comment                                                      |
| --------- | ------------------- | ------------------------------------------------------------ |
| `i`       | `( -- str)`         | Pushes a line from STDIN as a single string. |
| `y`       | `( -- str str str)` | Pushes a line from STDIN as multiple strings, separated by whitespace.          |
| `ɪ`       | `( -- int)`         | Pushes an integer from STDIN. Will NOP when it cannot find an integer. |
| `ʏ`       | `( -- float)`       | Pushes a float from STDIN. Will NOP when it cannot find a float. |
| `o`       | `(ele -- )`         | Pops and outputs to STDIN. Does not cast. |
| `ɤ`       | `(ele -- )`         | Pops and outputs to STDIN. Will cast lists to strings. |

## Functions

Functions are not actually true "functions", per se, since they do not take input, and are more like procedures since they act directly on the stack. They are most analogous to Forth definitions in declaration and use.

Functions must be declared before they are called. If not, the interpreter will ignore the call.

Functions are declared and called as the following, whitespace omitted:
```
<name>/code\
<name>
```
Function `name`s are strings of any non-whitespace characters that are not `>`.  They are also case sensitive.

Functions can be overwritten by declaring them again with `<name>/new code\`.

Functions can be declared in functions, however any functions within

## Control Structures

Control structures in IPEL change where the instruction pointer goes next.


| Character  | Stack Effect | Comment                                                      |
| ---------- | ------------ | ------------------------------------------------------------ |
| `ʌ`        | `(con -- )`  | Conditional Skip: If `con` is truthy, skip the next instruction. |
| `\|label\|` | `( -- )`     | Label: Signifies a label at the location of `❬label❭` with the name `str`. |
| `ʟ\|label\|` | `( -- )`     | Go-To Label: Jumps execution to the instruction after `\|label\|`. |

### Conditional Skip

The Conditional Skip pops the currently voiced stack for a value `con`. If `con` is truthy, the next instruction will be skipped.

### Labels and Go-To Label

Labels allow for arbitrary destinations for jumps in execution within an IPEL program.

Labels are delimited by pipes `|label|`. Labels can have any string within the brackets, stopping at the first `|`.

`ʟ` before a label will unconditionally jump the execution pointer to the given label.

Conditional jumps can be created using a combination of comparison/logical operators, a conditional skip, labels, and a `ʟ`.