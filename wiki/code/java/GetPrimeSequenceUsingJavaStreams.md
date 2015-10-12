<!-- title: Get a prime number sequence using Java 8 Streams  -->

With a spirit of expanding on my previous post about
[checking numbers for primality](CheckNumberPrimalityUsingJavaStreams), here's a
quick way to generate a sequence of prime numbers using streams:

    public static LongStream primeSequence(long max) {
        return LongStream.iterate(2, i -> i + 1)
                .filter(x -> isPrime(x))
                .limit(max);
    }

The above returns a `LongStream` of prime numbers up to a specified `max`
value. It uses my previous prime checker function `isPrime`.
