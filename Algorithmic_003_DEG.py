#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Degree Array
Rosalind ID: DEG
Algorithmic Heights #: 003
URL: http://rosalind.info/problems/deg/
'''


def degree_array(n, edges):
    '''Returns an array where index i represents the degree of node i+1.'''
    # Initialize the degree array.
    degrees = [0]*n

    # Add each edge to the degree array.
    for edge in edges:
        for node in edge:
            degrees[node-1] += 1

    return degrees


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_deg.txt') as input_data:
        n, m = map(int, input_data.readline().strip().split())
        edges = [map(int, line.strip().split()) for line in input_data.readlines()]

    # Get the degree array.
    deg_array = degree_array(n, edges)

    # Print and save the answer.
    print ' '.join(map(str, deg_array))
    with open('output/algorithmic/Algorithmic_003_DEG.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, deg_array)))


if __name__ == '__main__':
    main()
