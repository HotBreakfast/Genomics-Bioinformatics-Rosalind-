#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Complementing a Strand of DNA
Rosalind ID: REVC
Rosalind #: 003
URL: http://rosalind.info/problems/revc/
'''

from string import maketrans


def reverse_complement_dna(dna):
    '''Returns the reverse complement of the given DNA strand.'''
    transtab = maketrans('ATCG', 'TAGC')
    return dna.translate(transtab)[::-1]


def main():
    '''Main call. Parses, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_revc.txt') as input_data:
        dna = input_data.read().strip()

    # Get the reverse complement.
    rev_comp = reverse_complement_dna(dna)

    # Print and save the answer.
    print rev_comp
    with open('output/003_REVC.txt', 'w') as output_data:
        output_data.write(rev_comp)

if __name__ == '__main__':
    main()
