# International Phonetic Esoteric Language

## What is this?

The International Phonetic Esoteric Language (IPEL) is a personal project of mine to create a simple, stack-based esoteric programming language from scratch to challenge myself. I also decided to base its instruction set on the International Phonetic Alphabet by the International Phonetic Association, modeling the appearance of a typical phonetic transcription, such as `/hε.lɔ.wɔɹld/` for a rough approximation of "hello world".

It is meant for code golf, and is definitely not made for any sort of serious use.

## Installation

Install this by cloning this repository (`https://github.com/bigyihsuan/International-Phonetic-Esoteric-Language`).

## Execution

Execute the IPEL code by navigating to the repository folder and running `interpreter.py` with Python 3.

```
$ python3 interpreter.py [options] (codeFile | code)
```

`codeFile` is any file that contains IPEL code.
`code` is a string that contains IPEL code.

`[options]` is one of the following:

* `-d`: Runs the interpreter in debug mode. The interpreter will print the label mappings and the parsed lexemes. It will also print the data and execution stacks after every instruction.

## Documentation
More information can be found at the [Esolangs wiki page](https://esolangs.org/wiki/International_Phonetic_Esoteric_Language) for this language.
An IPA chart containing the used IPA characters can be found in [this Google Sheet](https://docs.google.com/spreadsheets/d/1LV9KpMahMhYt73ZeXxkj4kYb3jLvCFYeUnyAg5oGUDs/edit?usp=sharing).
