#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Transcribing DNA into RNA
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''


def dna_to_rna(dna):
    '''Translates the given DNA sequence to an RNA sequence.'''
    return dna.replace('T', 'U')


def main():
    '''Main call. Parses, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_rna.txt') as input_data:
        dna = input_data.read().strip()

    # Translate the DNA sequence to an RNA sequence.
    rna = dna_to_rna(dna)

    # Print and save the answer.
    print rna
    with open('output/002_RNA.txt', 'w') as output_data:
        output_data.write(rna)

if __name__ == '__main__':
    main()
