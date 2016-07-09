#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Breadth-First Search
Rosalind ID: BFS
Algorithmic Heights #: 012
URL: http://rosalind.info/problems/bfs/
'''

from collections import defaultdict


def minimum_dist_bfs(n, edges):
    '''Performs a BFS to get the minimum distance to all nodes starting at node 1.'''
    # Build the graph.
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)

    # BFS to find the minimum distance to each node from node 1.
    min_dist = [0] + [-1]*(n-1)
    remaining = set(xrange(2, n+1))
    queue = [1]
    while queue:
        current = queue.pop(0)
        for node in graph[current]:
            if node in remaining:
                queue.append(node)
                remaining.discard(node)
                # Rosalind starts indices at 1 instead of 0.
                min_dist[node-1] = min_dist[current-1] + 1

    return min_dist


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_bfs.txt') as input_data:
        n = map(int, input_data.readline().strip().split())[0]
        edges = [map(int, line.strip().split()) for line in input_data]

    # Get the minimum distances.
    min_dist = map(str, minimum_dist_bfs(n, edges))

    # Print and save the answer.
    print ' '.join(min_dist)
    with open('output/algorithmic/Algorithmic_009_BFS.txt', 'w') as output_data:
        output_data.write(' '.join(min_dist))

if __name__ == '__main__':
    main()
