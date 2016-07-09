#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area,
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: Suboptimal Local Alignment
Rosalind Armory ID: SUBO
Rosalind Armory #: 014
URL: http://rosalind.info/problems/subo/
'''

from Bio import SeqIO
from scripts import HammingDistance

# Read the input data.
with open('data/armory/rosalind_subo.txt') as input_data:
    dna = [fasta.seq for fasta in SeqIO.parse(input_data, 'fasta')]

# Run LALIGN with +4/-8 Matrix, -8 Gap Open/Extend, and pick the 100% match.
r = 'AGTGCTTGGTCATGTCTGCCTTGGAGGTCTAGG'

# Count the number of occurences in each sequence.
count = [sum([HammingDistance(dna[seq_num][i:i+len(r)], r) <= 3 for i in xrange(len(dna[seq_num]) - len(r) + 1)]) for seq_num in xrange(2)]

# Print and save the answer.
print ' '.join(map(str, count))
with open('output/armory/Armory_014_SUBO.txt', 'w') as output_data:
    output_data.write(' '.join(map(str, count)))
