#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Encoding Suffix Trees
Rosalind ID: SUFF
Rosalind #: 074
URL: http://rosalind.info/problems/suff/
'''

from scripts import SuffixTree

# Most of the work is done by the SuffixTree class in the Data Structures script.
with open('data/rosalind_suff.txt') as input_data, open('output/074_SUFF.txt', 'w') as output_data:
    s = input_data.read().strip()
    output_data.write('\n'.join(SuffixTree(s).print_edges()))
