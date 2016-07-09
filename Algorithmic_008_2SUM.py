#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: 2SUM
Rosalind ID: 2SUM
Algorithmic Heights #: 008
URL: http://rosalind.info/problems/2sum/
'''

from collections import defaultdict


def two_sum(a, x):
    '''Returns indices i and j such that a[i] + a[j] = x if they exist, otherwise -1.'''
    # Hash the array, storing the indices corresponding to each element.
    elmt_hash = defaultdict(set)
    for index, e in enumerate(a):
        elmt_hash[e].add(index)

    # Loop over all elements in the hash, checking for the necessary element to complete 2sum.
    for e in elmt_hash:
        if x-e in elmt_hash:
            if x-e == e and len(elmt_hash[e]) > 1:
                # Rosalind indices start at 1.
                return sorted([elmt_hash[e].pop()+1, elmt_hash[e].pop()+1])
            elif x-e != e:
                # Rosalind indices start at 1.
                return sorted([elmt_hash[e].pop()+1, elmt_hash[x-e].pop()+1])

    # If the loop ends 2sum is not possible.
    return -1


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_2sum.txt') as input_data:
        k, n = map(int, input_data.readline().strip().split())
        arrays = [map(int, line.strip().split()) for line in input_data.readlines()]

    # Run the 2sum algorithm on each array, then format the results.
    indices_2sum = [two_sum(a, 0) for a in arrays]
    indices_2sum = [str(x) if type(x) is int else ' '.join(map(str, x)) for x in indices_2sum]

    # Print and save the answer.
    print '\n'.join(indices_2sum)
    with open('output/algorithmic/Algorithmic_008_2SUM.txt', 'w') as output_data:
        output_data.write('\n'.join(indices_2sum))

if __name__ == '__main__':
    main()
