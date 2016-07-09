#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Creating a Restriction Map
Rosalind ID: PDPL
Rosalind #: 086
URL: http://rosalind.info/problems/pdpl/
'''

from collections import Counter


def partial_digest(distances):
    '''Returns a set whose positive pairwise differences generate 'distances'.'''
    # Initialize variables.
    X = {0}
    width = max(distances)

    # Create lambda functions for multiset operations.
    new_dist = lambda y, S: Counter(abs(y-s) for s in S)
    containment = lambda a, b: all(a[x] <= b[x] for x in a)

    # Create the multiset which generates 'distances'.
    while len(distances) > 0:
        y = max(distances)
        if containment(new_dist(y, X), distances):
            X |= {y}
            distances -= new_dist(y, X)
        else:
            X |= {width - y}
            distances -= new_dist(width - y, X)

    return X


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_pdpl.txt') as input_data:
        distances = Counter(map(int,input_data.read().strip().split()))

    # Get the partial digest.
    X = sorted(list(partial_digest(distances)))

    # Print and save the answer.
    print ' '.join(map(str, X))
    with open('output/086_PDPL.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, X)))


if __name__ == '__main__':
    main()
