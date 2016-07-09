#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Rooted Binary Trees
Rosalind ID: ROOT
Rosalind #: 087
URL: http://rosalind.info/problems/root/
'''

CUNR = __import__('068_CUNR')


def count_rooted_binary_trees(n):
    '''Returns the number of unrooted binary trees with n leaves.'''
    # Can transform an unrooted binary tree into a rooted binary tree by inserting
    # a node into any of its 2*n - 3 edges.
    return CUNR.count_unrooted_binary_trees(n)*(2*n - 3) % 10**6


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_root.txt') as input_data:
        n = int(input_data.read().strip())

    # Get the number of unrooted binary trees.
    count = count_rooted_binary_trees(n)

    # Print and save the answer.
    print count
    with open('output/087_ROOT.txt', 'w') as output_data:
        output_data.write(str(count))

if __name__ == '__main__':
    main()
