#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Fibonacci Numbers
Rosalind ID: FIBO
Algorithmic Heights #: 001
URL: http://rosalind.info/problems/fibo/
'''


def fibonacci(n):
    '''Returns the nth Fibonacci number (seed values F_0 = 0, F_1 = 1).'''

    # Make sure we have the correct input data.
    if n < 0 or type(n) is not int:
        return -1

    # Only store the two most recent values.
    fib = [0, 1]
    for i in xrange(n - 1):
        fib[i % 2] = sum(fib)
    return fib[n % 2]


if __name__ == '__main__':

    # Read the input data.
    with open('data/algorithmic/rosalind_fibo.txt') as input_data:
        n = int(input_data.read().strip())

    # Get the nth Fibonacci number.
    fib_n = fibonacci(n)

    # Print and save the answer.
    print str(fib_n)
    with open('output/algorithmic/Algorithmic_001_FIBO.txt', 'w') as output_data:
        output_data.write(str(fib_n))
