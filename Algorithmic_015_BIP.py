#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Testing Bipartiteness
Rosalind ID: BIP
Algorithmic Heights #: 015
URL: http://rosalind.info/problems/bip/
'''

from collections import defaultdict
from itertools import imap


def check_bipartite(edge_list):
    '''Checks if a graph is bipartite, returning 1 if True, -1 if False.'''
    # Extract the number of nodes from the edge list.
    n = edge_list.pop(0)[0]

    # Build the graph.
    graph = defaultdict(list)
    for node1, node2 in edge_list:
        graph[node1].append(node2)
        graph[node2].append(node1)

    # Color the graph.
    red, blue = set(), set()
    remaining = set(range(1, n+1))
    while remaining:
        # Pick a starting node and color it red (arbitrary choice of color).
        queue = {remaining.pop()}
        red |= queue
        while queue:
            # Pick a current node and get its remaining children.
            current = queue.pop()
            new_nodes = {node for node in graph[current] if node in remaining}

            # Color the new nodes the opposite of the parent color.
            if current in red:
                blue |= new_nodes
            else:
                red |= new_nodes

            # Add the new nodes to the queue, remove them from remaining nodes.
            queue |= new_nodes
            remaining -= new_nodes

    # Check for a valid coloring.
    for e in imap(set, edge_list):
        if e <= red or e <= blue:
            return -1

    # Return True if we pass the coloring check.
    return 1


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_bip.txt') as input_data:
        input_data.readline()  # Ignore first two lines.
        input_data.readline()
        edge_lists = [edges.split('\n') for edges in input_data.read().strip().split('\n\n')]
        edge_lists = [[map(int, nodes.split()) for nodes in edges] for edges in edge_lists]

    # Check each edge list to see if it is bipartite.
    bipartite = map(check_bipartite, edge_lists)

    # Print and save the answer.
    print ' '.join(map(str, bipartite))
    with open('output/algorithmic/Algorithmic_015_BIP.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, bipartite)))

if __name__ == '__main__':
    main()
