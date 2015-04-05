<!-- title: Time-Saving Tips for Python -->

**Caveat: "Time saving" is a loose term** -- especially for a large and/or
growing codebase shared by many developers, you want to be careful that time
saved by one person in writing code (e.g. with clever one-liners) doesn't
grossly compromise time spent by other people in reading it, maintaining it, or
otherwise working with it. This answer addresses the question in terms of
broader productivity gains across a software team, as opposed to tips and tricks
to hack up throwaway Python code as quickly as possible.

**For idiomatic Python**, get comfortable with list comprehensions, generators,
decorators, and context managers.

- List comprehensions are often the most idiomatic way of creating and
   transforming lists.
- Generators are most often used for defining iterators cleanly, usually with
   less memory overhead than alternative solutions.
- Decorators are great for common setup/cleanup code, like authentication,
   caching, or timing. Some built-in decorators like @classmethod and @property
   are very useful when working with classes. See also:
   [What are common uses of Python decorators?](http://www.quora.com/What-are-common-uses-of-Python-decorators)
- Context managers are also handy for setup/cleanup code, for example in opening
   and closing files or tags (Quora uses these to make sure tags in HTML
   generated from WebNode are always closed). Another cool use case is setting
   some state for the duration of a code block, like flags for bypassing cache
   or for pipelining networked instructions.

**Familiarize yourself with all the methods of the most common data
structures**: lists, sets, dictionaries. Python has a lot of useful built-in
functionality for working with these data structures, like slicing for lists or
mathematical set operations with syntactic sugar for easy use on sets.

**Run code snippets at an iPython shell**. Take full advantage of the fact that
  Python has a great interactive shell -- test out your code snippets quickly
  and fiddle with syntax or logic 'til they work, inspect your objects and
  functions, time function calls, etc. Make sure to use iPython and not the
  standard Python shell, as iPython is much more powerful and has nice features
  like tab-completion and %history.

**Use a linter like PyFlakes, PyLint, or PyChecker**
[comparison here](http://stackoverflow.com/questions/1428872/pylint-pychecker-or-pyflakes). Better
yet, hook your linter into your editor so it checks as you go, similar to the
code analysis and automatic error or warning highlighting that Java IDEs do.

**Familiarize yourself with Python's standard libraries**, like `urllib2`,
`time` and `datetime`, `random`, `itertools`, `functools`, `re`, `collections`,
etc. [See Also](http://stackoverflow.com/questions/1453952/most-useful-python-modules-from-the-standard-library).

**Use `print` statements and `pdb` to debug**. `print` is particularly effective
to use in Python since you don't need to compile your code again to start
printing useful debug output. As for `pdb`, just dump this wherever you need to
start investigating your running program: `import pdb; pdb.set_trace();` and
step through/in, continue, or print values as you
please. [See also](http://docs.python.org/library/pdb.html).

**Adopt strong naming conventions to make your code more self-documenting**. For
example, if you have user ids and user objects in your codebase, always use
`_user_id` to refer to the former and `_user` to refer to the latter, so it's
always clear whether you're working with an int/long that is the id or an object
that is the full user object. (This is an example that is particularly salient
given Python's lack of static type annotations.) And unless you are using `_`
for i18n, use `_` to indicate values to be thrown away.

----

Run `pyflakes` and `pep8` as part of your tests.  This keeps your code from
getting weird. The `autopep8` package has an `-i` flag that will let you fix
many `pep8` mistakes. Consider `pylint` or something more configurable for
deeper control.

Package any and all library like things, and install them via `pip` instead of
keeping them in a single repository. Use virtualenv and pth files to link to
favor "checked out" libraries if they exist over pip installed libraries.  This
will let you edit your libraries in
place. [You can turn off pyc creation](http://stackoverflow.com/questions/154443/how-to-avoid-pyc-files) -
these aren't always beneficial.

Contribute to open source projects that have people writing code that you find
easy to read and useful.  You can learn a lot from them. Understand some python
syntactical sugar: list comprehensions, generators, and generator comprehensions
are all very helpful. Learn what methods produce iterators and when to use them
(e.g. dictionaries, xrange). Get an idea of what the standard library provides.
collections, for example, is a quite a treat.

Have people more familiar with different aspects of the language code review
your code.  I get a lot of mileage from working with people who know a lot of
python, and I like it when they review my code.

----

For generating a bunch of data that is similar but not the same, I recently ran
across this beginner's shortcut on Codeacademy using
[argument unpacking](http://www.codecademy.com/courses/function-call-concepts):

    class Dog:
        def __init__(self, name, age, breed, color):
            self.name = name
            self.gender = gender
            self.breed = breed
            self.color = color

    # create the defaults
    attrs = {"age": 7, "gender": "m", "breed": "mutt", "color": "motley"}

    #create boy dogs
    spuds = Dog("spuds", **attrs)
    spike = Dog("spike", **attrs)

    #modify sex and get all of the rest of the default data for free
    attrs["gender"] = "f"

    #create girl dogs
    laika = Dog("laika", **attrs)
    lassy = Dog("lassy", **attrs)


`**attrs` unpacks into the list init is expecting.

Super easy to throw this concept into a couple of loops and generate a bunch of
data files for testing various mechanisms that need valid (and invalid, as
needed) bulk data.

I suspect there are more efficient ways of doing this, and look forward to
reading about them in the comments.

----

**[Understand list comprehensions](http://docs.python.org/tutorial/datastructures.html#list-comprehensions)**:
many `for` loops can be written more clearly and succinctly with this language
construct.  Or, more generally ...

**[Understand generators](http://docs.python.org/reference/expressions.html#generator-expressions)**
since list comprehensions are essentially generators realized into a list.
Generator expressions can be used in many contexts where the naive way would be
to build a list in an additional code block. Once you understand generators,
learn about the
[itertools library](http://docs.python.org/library/itertools.html).

**Understand data structure capabilities**.  My favorite underutilized data
structures are [sets](http://docs.python.org/tutorial/datastructures.html#sets)
and [counters](http://docs.python.org/library/collections.html#counter-objects),
but there are many more.  Trying to conceptualize your problem in a mathematical
domain will often make the solution simple to write because of Python's famed
_psudo-code that runs_ aesthetic.  That aesthetic frequently comes from data
structure support for common operations.

**Learn another language**.  Clojure and Haskell (as examples) will force you to
write more succinct code in many cases, and that experience can translate to
better Python code.  Just make sure when you come back to Python, you follow
Python's social mores.

Here's an example that tries to tie these together: find the number of different
words between two pieces of text, `a_str` and `b_str`.

    a_words, b_words = [set(w.lower() for w in re.split('\W+', s)) for s in (a_str, b_str)]
    len(a_words ^ b_words)

A generator expression is used in the construction of two sets.  A list
comprehension is used to run a transformation over the two inputs.  Iterable
data structures can be _unpacked_ or _destructured_ into multiple variables.
The mathematical notion of set difference is used to find the set of different
words.

----

A few things not yet mentioned.

### enumerate()

Sometimes you want the items in a list and a counter.  The following are all
more or less equivalent.

    # Iterating with a counter
    for i in xrange(len(thelist)):
        v = thelist[i]
        ...

    # Keeping a counter
    i = 0
    for v in thelist:
        ...
        i += 1

    # Using enumerate
    for i, v in enumerate(thelist):
       ...


### defaultdict

Python's `collections` module has a bunch of very useful tools.  It's worth
exploring the package.  One of my favorites and more used is the `defaultdict`.
Let's say we have a list of values and we want to count occurrences of the items
in the list.  (Granted there's a `Counter` in collections now, but bear with
me.) These will work:

    # Naive way
    counter = {}
    for item in thelist:
        if item in counter:
            counter[item] += 1
        else:
            counter[item] = 0

    # Using get()
    counter = {}
    for item in thelist:
        counter[item] = counter.get(item, 0) + 1

    # Using defaultdict
    counter = defaultdict(int)
    for item in thelist:
        counter[item] += 1

As you can see, it's also handy to know about dict's `get()` method... and
`defaultdict` can work with many types.  Want a dict of lists? Use
`defaultdict(list)`.

### Embedding IPython

Using `pdb` has been mentioned, but I usually just like to break in at a
particular spot with an IPython shell and go from there to debug.  Remember
these two magic lines:

    import IPython
    IPython.embed()

That's it!  Just toss that in wherever you'd use `pdb`.

### Know your data types

Looking up an item in a list?  It's runtime is _O(n)_.

Looking up a key in a dict?  Runtime is _O(1)_.

What if you have a big list that you're going to do many lookups on in a loop
and you don't care about duplicates in the list?

    # This can be slow
    user_ids = get_user_ids_meeting_condition()
    for t in transactions:
        user_id = t['user_id']
        if user_id not in user_ids:
             continue
        ...

    # Speeding things up with a set
    user_ids = set(get_user_ids_meeting_condition())
    for t in transactions:
        user_id = t['user_id']
        if user_id not in user_ids:
             continue
        ...

Same code, but now `user_ids` is a `set` and lookups are _O(1)_ instead of
_O(n)_.  Moral of the story?  Don't forget about the set!

----

I assume time saving doesn't mean saving time right now but saving time later,
avoiding difficulties when debugging or refactoring code. In this context, time
saving tips could be:

- Never use `import *` or relative imports
- Avoid duplicate ascendant/descendant directory names in your tree.
- Avoid `locals()` and `globals()`
- Try hard to have no circular dependencies, import only on top of
  modules. Exceptions must have explanatory comment.
- Inside the same project, import at the source: do not import _x_ from _b_ if the
  actual code is in _a_.
- Do not use default param values when it is not used.
- Use `_private` methods and functions by default for method you don't use outside
  the module or the class.
- Listen carefully to most of what pylint will tell you, tweak its config if
  necessary.
- Do not pass variables just in case they might be used in the future. Python is
  very ductile, adding something later is almost always easier than removing
  later something that might it might not be useless.
- Never ever write testable code without the tests.

----

Quick simple debugging:

    import pdb
    pdb.set_trace()

Tracing live code:

    $ python -m trace --trace myModule.py

----

**If you're running Python code via a console (eg unit tests), you might find
the below recipe useful**:
[it automatically starts the debugger on an exception](http://code.activestate.com/recipes/65287/). Place
the code in the path `LIB/python2.X/sitecustomize.py` for this to work.

    import bdb
    import sys

    def info(type, value, tb):
      if hasattr(sys, 'ps1') \
          or not sys.stdin.isatty() \
          or not sys.stdout.isatty() \
          or not sys.stderr.isatty() \
          or issubclass(type, bdb.BdbQuit) \
          or issubclass(type, SyntaxError):
        # we are in interactive mode or we don't have a tty-like
        # device, so we call the default hook
        sys.__excepthook__(type, value, tb)
      else:
        import traceback, pdb
        # we are NOT in interactive mode, print the exception...
        traceback.print_exception(type, value, tb)
        print
        # ...then start the debugger in post-mortem mode.
        pdb.pm()

    sys.excepthook = info


The version provided here is a little modified based on the comments on the
recipe; [it is available as a gist](https://gist.github.com/rctay/3169104).

----

**Document your code with comments:**
This should be self explanatory but it will help dramatically. There is a fine
line between doing it right and having way too many comments. What I like to do
is, for every module I have a docstring at the top and for every function/method
which is not extremely self explanatory (e.g. a property which returns an
underlying variable) I will have a short description and describe the arguments
and return value. This seems useless at times but it will make your code so much
more maintainable and readable to a third party and yourself.

**Use the same style throughout:**
The way I think about this is if I were to write a book, I would try to keep the
same style all the way through. If I choose to use the oxford comma then I'll
continue using it. If I put two spaces after a period I'll continue doing
that. I find the same with python especially because white spaces matter and
there tend to be a lack of parentheses and brackets to wrap statements. So I try
to follow 80 characters per line and when I have line breaks I try to follow the
same conventions, especially when passing a lot of arguments to functions. This
way it makes it far easier to read when I come back to it.

**Use some sort of IDE:**
Whether it is plugins to VIM or full fledged PyCharm, use something where
jumping to different modules is simple. I use sublime text 2 and it's pretty
excellent.
