#!/usr/bin/env python
"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Point Mutations
Rosalind ID: HAMM
Rosalind #: 006
URL: http://rosalind.info/problems/hamm/
"""

from itertools import imap
from operator import ne


def hamming_distance(seq1, seq2):
    'Returns the Hamming distance between equal-length sequences.'
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(imap(ne, seq1, seq2))


def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Read the input data.
    with open('data/rosalind_hamm.txt') as input_data:
        seq1, seq2 = [line.strip() for line in input_data]

    # Get the Hamming Distance.
    h_dist = str(hamming_distance(seq1,seq2))

    # Print and save the answer.
    print h_dist
    with open('output/.txt', 'w') as output_data:
        output_data.write(h_dist)

if __name__ == '__main__':
    main()
