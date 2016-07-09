#!/usr/bin/env python
"""
ROSALIND bioinformatics scripts for DNA and RNA sequences.
Not necessarily solutions to entire problems, but small things
that appear in multiple problems.
"""

from itertools import imap
from operator import ne
from string import maketrans


def DNA_to_RNA(dna):  # Kind of pointless, as it's so simple.
    '''Translates DNA to RNA'''
    return dna.replace('T', 'U')


def RNA_to_DNA(rna):  # Kind of pointless, as it's so simple.
    '''Translates RNA to DNA'''
    return rna.replace('U', 'T')


def ReverseComplementDNA(dna):
    '''Returns the reverse complement of a given DNA strand.'''
    transtab = maketrans('ATCG', 'TAGC')
    return dna.translate(transtab)[::-1]


def ReverseComplementRNA(rna):
    '''Returns the reverse complement of a given RNA strand.'''
    transtab = maketrans('AUCG', 'UAGC')
    return rna.translate(transtab)[::-1]


def hamming_distance(seq1, seq2):
    'Returns the Hamming distance between equal-length sequences.'
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(imap(ne, seq1, seq2))
