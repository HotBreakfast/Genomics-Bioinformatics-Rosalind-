#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Bellman-Ford Algorithm
Rosalind ID: BF
Algorithmic Heights #: 022
URL: http://rosalind.info/problems/bf/
'''


def bellman_ford(n, edges, source):
    '''Uses the Bellman-Ford Algorithm to get the distances from a source node to all other nodes.'''
    # Initialize distances.  Recall: Rosalind indicies start at 1.
    dist = [float('inf') if i != source-1 else 0 for i in xrange(n)]

    # Run the Bellman-Ford updated procedure |V|-1 times.
    for i in xrange(n-1):
        # Relaxation condition to break outer look early.
        relaxed = True
        for u, v, weight in edges:
            if dist[u-1] + weight < dist[v-1]:
                dist[v-1] = dist[u-1] + weight
                relaxed = False
        if relaxed:
            break

    # Return the distances in the desired format.
    return [d if d != float('inf') else 'x' for d in dist]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_bf.txt') as input_data:
        n = map(int, input_data.readline().strip().split())[0]
        edges = [map(int, line.strip().split()) for line in input_data]

    # Get the minimum distances using the Bellman-Ford Algorithm.
    distances = map(str, bellman_ford(n, edges, 1))

    # Print and save the answer.
    print ' '.join(distances)
    with open('output/algorithmic/Algorithmic_022_BF.txt', 'w') as output_data:
        output_data.write(' '.join(distances))

if __name__ == '__main__':
    main()
