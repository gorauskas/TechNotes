<!-- title: Smash Into VIM -->

Philosophy: These two ideas distinguish `vim` from other text editors:

1. *Modal Editing*: This is all about editing text efficiently. You spend more
   time moving through existing text and editing it than you do inserting fresh
   blocks of text. Navigation and editing is as easy as typing it fresh. Ignore
   the modes: think about giving `vim` commands in series
2. *Operator Command Pattern*: The commands that you can give `vim` follow a
   certain pattern.

For example:

    d2w

Here's the explanation for the above:

    d = delete operator
    2 = two count
    w = words motion
