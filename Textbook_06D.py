#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Shared k-mers Problem
Rosalind ID: 6D
URL: http://rosalind.info/problems/6d/
'''

from collections import defaultdict
from scripts import ReverseComplementDNA as rev_comp


def shared_kmers(k, dna1, dna2):
    '''Returns a list of positions for shared k-mers (up to reverse complement) in dna1 and dna2.'''
    # Store the starting index of all k-mers from dna1 in a dictionary keyed to the k-mer.
    dna1_dict = defaultdict(list)
    for i in xrange(len(dna1)-k+1):
        dna1_dict[dna1[i:i+k]].append(i)

    # Check k-mers in dna2 against those in dna1, add matching index pairs to a set to remove possible duplicate entries.
    return {(i,j) for j in xrange(len(dna2)-k+1) for i in dna1_dict[dna2[j:j+k]] + dna1_dict[rev_comp(dna2[j:j+k])]}


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data/textbook/rosalind_6d.txt') as input_data:
        k = int(input_data.readline().strip())
        dna1, dna2 = [line.strip() for line in input_data.readlines()]

    # Get the shared k-mers.  Sorting doesn't add significant time and makes the result more readable.
    shared_kmer_indices = map(str, sorted(shared_kmers(k, dna1, dna2)))

    # Print and save the answer.
    # print '\n'.join(shared_kmer_indices)
    with open('output/textbook/Textbook_06D.txt', 'w') as output_data:
        output_data.write('\n'.join(shared_kmer_indices))

if __name__ == '__main__':
    main()
