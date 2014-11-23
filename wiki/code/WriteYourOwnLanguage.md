<!-- title: So, you want to write your own language? -->

Below are my notes from a really interesting article about the creation of
programming languages by Walter Bright published on January 21, 2014 in the
Dr. Dobbs Journal.

[http://www.drdobbs.com/architecture-and-design/so-you-want-to-write-your-own-language/240165488](http://www.drdobbs.com/architecture-and-design/so-you-want-to-write-your-own-language/240165488)

### Work

Tons of work ... years of work ... need intrinsic motivation. Not a major cash
investment

### Design

Syntax matters a lot.  It needs to be something that appeals to your target
audience.  A mix of familiar syntax + aesthetic beauty.

These should NOT be considerations:

- Minimizing keystrokes
- Easy parsing. not hard to write parsers with arbitrary lookahead
- Minimizing the number of keywords

These things are TRULY GOOD:

- Context-Free Grammar. code is parsable without having to look up in a symbol
  table
- Redundancy. the grammar should be redundant to get good error messages
- Tried and True. Stick with tried and true grammatical forms. cuts the learning
  curve. e.g. people expect + and * to follow a certain precedence rule.

After syntax, the important thing is semantic processing... meaning is assigned
here to syntax structure.  This is where you spend most of the design and
implementation time.  There is no glory in the semantics, but it is the whole
point of the language.

After the semantice phase, the compiler does optimizations and code generation
This is collectively called the back-end.  Very challenging and complicated
these 2 phases.  Try using an existing back end such as one of JVM, CLR, GCC,
LLVM.

### Implementation

Regex is the wrong tool for lexing and parsing.

Don't bother wasting time with lexer and parser generators or other so-called
*compiler compilers*. They are a waste of time.  Writing the lexer and the
parser is a tiny percentage of the job of writing a compiler.

Error messages are a big factor in the quality of implementation of the
language. Use the following guidelines:

- print the first error message and quit
- guess what a programmer intended, repair the AST and continue
- The poisoning approach. any operation with a NaN results in a NaN silently.

Compiler speed matters a lot... Most compilers are pigs.  The secret to making a
compiler fast is to use a *profiler*.

You must/have to be using these tools in order to be successful:

- valgrind. saved C and C++ from oblivion
- git / github like public repo. trasnformative tools. collaboration. track the
  origin of every line of code
- Automated testing framework + Coverage analyzer
- Automated documentation generator
- Bugtracker + Wiki + Blog + Google Groups + Mailing List + IRC Channel +
  Twitter + Facebook

### Lowering

A semantic technique. It consists of, internally, rewrting more complex semantic
constructs in terms of simpler ones. e.g. *while* loops and *foreach* loops can
be rewritten in terms of *for* loops. Then the rest of the code only has to deal
with *for* loops. If there are special-case rules in the language that prevent
*lowering* rewriting, then revisit the design of the language.

### Runtime Library

Critical is the need to write a runtime library.  This is a major project.  It
serves as the demostration of how the language features work.  It better be
good.

Get these right:

- I/O performance. Slow IO will make that language look bad. the benchmark is C
  stdio
- Memory allocation. Most of the time programs spend doing this
- Transcendental functions... What are these? Find a library that already
  implements these functions ... Floating point stuff

#### What should go in a library

- File IO
- Network IO
- String
- Algorithms
- Data Structures
- OS Interaction
- Unicode - UTF-8
- Date / Time
- Memory Management
- Process Control
- Signals
- Math
- Data Types
- Crypto
- Reflection

### After the Prototype

- Presentations
- Articles
- Tutorials
- Books
- Programmer Meetings
- Conferences
- Companies

Go anywhere they will have you and show it off.  Get used to public speaking.
Get as much feedback as you can.
