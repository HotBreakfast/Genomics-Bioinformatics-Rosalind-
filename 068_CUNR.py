#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Unrooted Binary Trees
Rosalind ID: CUNR
Rosalind #: 068
URL: http://rosalind.info/problems/cunr/
'''


def count_unrooted_binary_trees(n):
    '''Returns the number of unrooted binary trees with n leaves.'''
    # The total number is just the double factorial (2n -5)!!
    return reduce(lambda a, b: a*b % 10**6, xrange(2*n-5, 1, -2))


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_cunr.txt') as input_data:
        n = int(input_data.read().strip())

    # Get the number of unrooted binary trees.
    count = count_unrooted_binary_trees(n)

    # Print and save the answer.
    print count
    with open('output/068_CUNR.txt', 'w') as output_data:
        output_data.write(str(count))

if __name__ == '__main__':
    main()
