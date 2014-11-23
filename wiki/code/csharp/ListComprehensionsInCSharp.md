<!-- title: List Comprehensions In CSharp -->

A *List Comprehension* is a type of set notation in which the programmer can
describe the properties that the members of a set must meet. It is usually used
to create a set based on other, already existing, set or sets by applying some
type of combination, transform or reduction function to the existing set(s).

Consider the following problem: You have a sequence of 10 numbers from 0 to 9
and you need to extract all the even numbers from that sequence. In a language
such a C# version 1.1, you were pretty much confined to the following code to
solve this problem:

    ArrayList evens = new ArrayList();
    ArrayList numbers = Range(10);
    int size = numbers.Count;
    int i = 0;

    while (i < size) {
        if (i % 2 == 0) {
            evens.Add(i);
        }
        i++;
    }

The code above does not show the implementation of the `Range` function, which
is available in the full code listing below. With the advent of C# 3.0 and the
.NET Framework 3.5, a List Comprehension notation based on Linq is now available
to C# programmers. The above C# 1.1 code can be ported to C# 3.0 like so:

    IEnumerable<int> numbers = Enumerable.Range(0, 10);
    var evens = from num in numbers where num % 2 == 0 select num;

And technically speaking, the C# 3.0 code above could be written as a one-liner
by moving the call to `Enumarable.Range` into the Linq expression that generates
the `evens` sequence.  In the C# List Comprehension I am reducing the set
`numbers` by applying a function (the modulo 2) to that sequence.  This produces
the `evens` sequences in a much more concise manner and avoid the use of loop
syntax. Now, you may ask yourself: Is this purely syntax sugar? I don't know,
but I will definitelly investigate, and maybe even ask the question myself at
[StackOverflow][lnk1]. I suspect that this is not just syntax sugar and that
there are some true optimizations that can be done by utilizing the underlying
Monads.

I also posted this as [an answer to a question][lnk2] on
[StackOverflow.com][lnk1]. The full code listing is available below:

    using System;
    using System.Collections;
    using System.Collections.Generic;
    using System.Linq;

    namespace CSharpListComprehensions {
        public class Program {

            public static void RunSnippet() {
                Run11Version();
                Run35Version();
            }

            public static void Run11Version() {
                ArrayList evens = new ArrayList();
                ArrayList numbers = Range(10);
                int size = numbers.Count;
                int i = 0;

                WL(""); WL("Numbers:");
                foreach (int x in numbers) {
                    WL(x.ToString());
                }

                while (i < size) {
                    if (i % 2 == 0) {
                        evens.Add(i);
                    }
                    i++;
                }

                WL(""); WL("Evens:");
                foreach (int y in evens) {
                    WL(y.ToString());
                }
            }

            public static void Run35Version() {
                IEnumerable<int> numbers = Enumerable.Range(0, 10);

                WL(""); WL("Numbers:");
                foreach (int x in numbers) {
                    WL(x.ToString());
                }

                var evens = from num in numbers where num % 2 == 0 select num;

                WL(""); WL("Evens:");
                foreach (int y in evens) {
                    WL(y.ToString());
                }
            }

            #region Range Function
            public static ArrayList Range(int end) {
                return Range(0, end);
            }

            public static ArrayList Range(int start, int end) {
                ArrayList al = new ArrayList();
                for (int i = start; i < end; i++) {
                    al.Add(i);
                }

                return al;
            }
            #endregion

            #region Helper methods

            public static void Main() {
                try {
                    RunSnippet();
                } catch (Exception e) {
                    string error = string.Format("---\nThe following error occurred while executing the snippet:\n{0}\n---", e.ToString());
                    Console.WriteLine(error);
                } finally {
                    Console.Write("Press any key to continue...");
                    Console.ReadKey();
                }
            }

            private static void WL(object text, params object[] args) {
                Console.WriteLine(text.ToString(), args);
            }

            private static void RL() {
                Console.ReadLine();
            }

            private static void Break() {
                System.Diagnostics.Debugger.Break();
            }

            #endregion
        }
    }


[lnk1]: http://stackoverflow.com/ "Stack Overflow"
[lnk2]: http://stackoverflow.com/questions/130898 "SO Question"
