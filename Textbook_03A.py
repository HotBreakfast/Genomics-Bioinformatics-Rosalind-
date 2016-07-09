#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Motif Enumeration
Chapter #: 03
Problem ID: A
URL: http://rosalind.info/problems/3a/
'''

from Textbook_01G import MismatchList


def motif_enumeration(k, d, dna_list):
    '''Returns all (k, d)-motifs that are shared by all sequences in dna_list.'''

    # Generate sets of (k,d)-motifs for each dna sequence in the list.
    motif_sets = [{kmer for i in xrange(len(dna)-k+1) for kmer in MismatchList(dna[i:i+k], d)} for dna in dna_list]

    # Intersect all sets to get the common elements.  The answers are displayed as sorted, so we'll sort too.
    return sorted(list(reduce(lambda a,b: a & b, motif_sets)))


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data/textbook/rosalind_3a.txt') as input_data:
        k, d = map(int, input_data.readline().split())
        dna_list = [line.strip() for line in input_data.readlines()]

    # Get the motifs.
    motifs = motif_enumeration(k, d, dna_list)

    # Print and save the answer.
    print ' '. join(motifs)
    with open('output/textbook/Textbook_03A.txt', 'w') as output_data:
        output_data.write(' '.join(motifs))

if __name__ == '__main__':
    main()
