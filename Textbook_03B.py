#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Median String Problem
Chapter #: 03
Problem ID: B
URL: http://rosalind.info/problems/3b/
'''

from itertools import product
from scripts import HammingDistance


def median_string(k, dna_list):
    # Initialize the best pattern score as one greater than the maximum possible score.
    best_score = k*len(dna_list) + 1

    # Check the scores of all k-mers.
    for pattern in product('ACGT', repeat=k):
        current_score = sum([motif_score(''.join(pattern), dna) for dna in dna_list])
        if current_score < best_score:
            best_score = current_score
            best_pattern = ''.join(pattern)

    return best_pattern


def motif_score(pattern, motif):
    '''Returns the score of d(pattern, motif).'''
    return min([HammingDistance(motif[i:i+len(pattern)], pattern) for i in range(len(motif)-len(pattern)+1)])


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_3b.txt') as input_data:
        k = int(input_data.readline())
        dna_list = [line.strip() for line in input_data.readlines()]

    # Get the best pattern.
    best_pattern = median_string(k, dna_list)

    # Print and save the answer.
    print best_pattern
    with open('output/textbook/Textbook_03B.txt', 'w') as output_data:
        output_data.write(best_pattern)

if __name__ == '__main__':
    main()
