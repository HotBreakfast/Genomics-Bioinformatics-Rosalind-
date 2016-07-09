#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Double-Degree Array
Rosalind ID: DDEG
Algorithmic Heights #: 005
URL: http://rosalind.info/problems/ddeg/
'''

from collections import defaultdict


def double_degree_array(n, edges):
    '''Return the double degree array associated with n nodes and the edges between them.'''
    # Create a dictionary storing the neighbors of each node.
    neighbors = defaultdict(list)
    for n1, n2 in edges:
        neighbors[n1].append(n2)
        neighbors[n2].append(n1)

    # Returns the sum of the degrees of a given nodes neighbors
    neighbor_deg_sum = lambda node: sum([len(neighbors[neighbor]) for neighbor in neighbors[node]])

    # Build and return the double degree array.
    return [neighbor_deg_sum(i) for i in xrange(1, n+1)]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_ddeg.txt') as input_data:
        n = map(int, input_data.readline().strip().split())[0]
        edges = [map(int, line.strip().split()) for line in input_data]

    # Get the double degree array.
    ddeg = map(str, double_degree_array(n, edges))

    # Print and save the answer.
    print ' '.join(ddeg)
    with open('output/algorithmic/Algorithmic_005_DDEG.txt', 'w') as output_data:
        output_data.write(' '.join(ddeg))

if __name__ == '__main__':
    main()
