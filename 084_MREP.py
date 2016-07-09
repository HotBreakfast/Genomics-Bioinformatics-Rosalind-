#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Identifying Maximal Repeats
Rosalind ID: MREP
Rosalind #: 084
URL: http://rosalind.info/problems/mrep/
'''

from scripts import SuffixTree

# Read the input data.
with open('data/rosalind_mrep.txt') as input_data:
    dna = input_data.read().strip()

# Create the Suffix Tree.
suff = SuffixTree(dna)

# Store all multiple repeats of length at least 20 in a dictionary keyed on number of appearances.
repeat_dict = {}
for node in suff.nodes[1:]:
    if suff.total_descendants(node) >= 2 and len(suff.node_word(node)) >= 20:
        if suff.total_descendants(node) not in repeat_dict:
            repeat_dict[suff.total_descendants(node)] = [suff.node_word(node)]
        else:
            repeat_dict[suff.total_descendants(node)].append(suff.node_word(node))

# Filter out non-maximal repeats.
repeats = []
for values in repeat_dict.values():
    if len(values) == 1:
        repeats += values
    else:
        repeats += filter(lambda v: reduce(lambda a, b: a*b, [v not in word for word in values if word != v]), values)

# Print and save the answer.
print '\n'.join(repeats)
with open('output/084_MREP.txt', 'w') as output_data:
    output_data.write('\n'.join(repeats))
