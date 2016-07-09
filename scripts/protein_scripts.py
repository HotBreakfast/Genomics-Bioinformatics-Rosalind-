#!/usr/bin/env python
'''A ROSALIND bioinformatics script to create RNA and DNA to Protein dictionary.'''

import os


class ProteinTranslator(object):
    """Performs various protein related translations."""
    def __init__(self):
        """Initialize the translation dictionaries."""
        # Build the dna to protein dictionary.
        with open(os.path.join(os.path.dirname(__file__), 'data/codon_table_dna.txt')) as dna_prot_table:
            self.dna_to_protein_dict = {line.strip().split()[0]:line.strip().split()[1] for line in dna_prot_table}

        # Build the rna to protein dictionary.
        with open(os.path.join(os.path.dirname(__file__), 'data/codon_table_rna.txt')) as rna_prot_table:
            self.rna_to_protein_dict = {line.strip().split()[0]:line.strip().split()[1] for line in rna_prot_table}

        # Read the protein masses and add them to a dictionary.
        with open(os.path.join(os.path.dirname(__file__), 'data/protein_mass_table.txt')) as prot_weight_table:
            self.protein_weight_dict = {line.strip().split()[0]:float(line.strip().split()[1]) for line in prot_weight_table.readlines()}

    def dna_to_protein(self, base):
        return self.dna_to_protein_dict[base]

    def rna_to_protein(self, base):
        return self.rna_to_protein_dict[base]

    def protein_weight(self, prot):
        return self.protein_weight_dict[prot]
