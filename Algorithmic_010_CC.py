#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Connected Components
Rosalind ID: CC
Algorithmic Heights #: 010
URL: http://rosalind.info/problems/cc/
'''

from collections import defaultdict


def connected_component_count(n, edges):
    '''Performs a BFS to get the number of connected components.'''
    # Build the graph.
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)
        graph[n2].append(n1)

    # Traverse the graph to find the number of connected components.
    component_count = 0
    remaining = set(xrange(1, n+1))
    while remaining:
        component_count += 1
        queue = {remaining.pop()}
        while queue:
            current = queue.pop()
            new_nodes = {node for node in graph[current] if node in remaining}
            queue |= new_nodes
            remaining -= new_nodes

    return component_count


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_cc.txt') as input_data:
        n = map(int, input_data.readline().strip().split())[0]
        edges = [map(int, line.strip().split()) for line in input_data]

    # Get the minimum distances.
    cc_count = str(connected_component_count(n, edges))

    # Print and save the answer.
    print cc_count
    with open('output/algorithmic/Algorithmic_010_CC.txt', 'w') as output_data:
        output_data.write(cc_count)

if __name__ == '__main__':
    main()
