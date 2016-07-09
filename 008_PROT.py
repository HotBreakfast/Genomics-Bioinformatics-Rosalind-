#!/usr/bin/env python
"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Translating RNA into Protein
Rosalind ID: PROT
Rosalind #: 008
URL: http://rosalind.info/problems/prot/
"""

from itertools import imap, takewhile
from scripts import ProteinTranslator


def rna_to_protein(rna):
    """Translates RNA to Protein."""
    # Load the translator and create a lambda function to check for the stop codon.
    translate = ProteinTranslator()
    not_stop = lambda rna_base: translate.rna_to_protein(rna_base) != 'Stop'

    # Generate a list of all rna triples up to the stop codon, then translate to protein.
    non_stop_rna = takewhile(not_stop, (rna[3*i:3*i+3] for i in xrange(len(rna)/3)))
    protein_list = imap(translate.rna_to_protein, non_stop_rna)

    return ''.join(protein_list)


def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Read the input data.
    with open('data/rosalind_prot.txt') as input_data:
        s = input_data.read().strip()

    # Get the translated protein.
    protein_output = rna_to_protein(s)

    # Print and save the answer.
    print protein_output
    with open('output/008_PROT.txt', 'w') as output_data:
        output_data.write(protein_output)

if __name__ == '__main__':
    main()
