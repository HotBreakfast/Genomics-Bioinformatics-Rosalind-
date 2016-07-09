#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Catalan Numbers and RNA Secondary Structures
Rosalind ID: CAT
Rosalind #: 033
URL: http://rosalind.info/problems/cat/
'''

from scripts import ReadFASTA


def noncrossing_perfect_bondings(rna):
    '''Returns the number of noncrossing perfect bondings for the given RNA sequence'''
    # Initialize dictionaries.
    bonding = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
    noncrossing_bondings = {}

    def count_noncrossing(rna):
        '''Recursively computes the number of noncrossing perfect bondings for a given RNA sequence'''
        if len(rna) <= 2:  # We only send valid rna matchings, so this return is ok.
            return 1
        elif rna in noncrossing_bondings:  # If we've already computed the value, return it!
            return noncrossing_bondings[rna]

        # Determine valid locations where the RNA can be split while maintaining necessary noncrossing conditions.
        splits = [i for i in xrange(1, len(rna), 2) if rna[0] == bonding[rna[i]] and check_subinterval(rna[1:i])]

        # Reduce the problem to noncrossing matchings over the subintervals.
        noncrossing_bondings[rna] = sum([count_noncrossing(rna[1:i])*count_noncrossing(rna[i+1:]) for i in splits]) % 1000000

        return noncrossing_bondings[rna]

    return count_noncrossing(rna)


def check_subinterval(subint):
    '''Checks if a given subinterval has the same number of matching nucleotides.'''
    N = [subint.count(nucleotide) for nucleotide in 'AUCG']
    return N[0] == N[1] and N[2] == N[3]  # Necessary for a noncrossing perfect bonding.


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Parse the input data.
    rna = ReadFASTA('data/rosalind_cat.txt')[0][1]

    # Get the number of noncrossing perfect bondings.
    noncrossing = str(noncrossing_perfect_bondings(rna))

    # Print and save the answer.
    print noncrossing
    with open('output/033_CAT.txt', 'w') as output_file:
        output_file.write(str(noncrossing))

if __name__ == '__main__':
    main()
