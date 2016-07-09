#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Using the Spectrum Graph to Infer Peptides
Rosalind ID: SGRA
Rosalind #: 073
URL: http://rosalind.info/problems/sgra/
'''

from scripts import ProteinWeightDict
from Textbook_05D import topological_ordering


def find_weight_match(approx_weight, error):
    for item in ProteinWeightDict().items():
        if abs(item[1] - approx_weight) < error:
            return item[0]
    return None


def infer_longest_peptide(masses):
    '''Returns the longest protein string that matches the spectrum graph of the given masses.'''
    # Build the graph from the given masses.
    graph = dict()
    protein_weight_dict = ProteinWeightDict()
    for i in xrange(len(masses)):
        for j in xrange(i+1, len(masses)):
            # Break the inner loop if we've exceeded the maximum weight.
            if masses[j] - masses[i] > max(protein_weight_dict.values()) + 1:
                break

            # Check if the weight associated with masses i and j approximately matches a known protein.
            temp_protein = find_weight_match(masses[j] - masses[i], 0.001)
            if temp_protein is not None:
                graph[masses[i], masses[j]] = temp_protein

    # Get the topological ordering of the graph.
    top_order = topological_ordering(graph.keys())

    # Build the longest path to each node.
    S = {node: '' for node in top_order}
    for node in top_order:
        for predecessor in map(lambda n: n[0], filter(lambda e: e[1] == node, graph.keys())):
            if len(S[predecessor]) + 1 > len(S[node]):
                S[node] = S[predecessor] + graph[(predecessor, node)]

    # Return the longest path.
    return max(S.values(), key=len)


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/rosalind_sgra.txt') as input_data:
        masses = [float(line.strip()) for line in input_data.readlines()]

    # Get the longeset peptide.
    peptide = infer_longest_peptide(masses)

    # Print and save the answer.
    print peptide
    with open('output/073_SGRA.txt', 'w') as output_data:
        output_data.write(peptide)

if __name__ == '__main__':
    main()
