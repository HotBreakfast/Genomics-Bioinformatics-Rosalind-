#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Trie Construction Problem
Rosalind ID: 7A
URL: http://rosalind.info/problems/7a/
'''

from scripts import Trie


def trie_edges(words):
    '''Returns the edges of a trie constructed from the given words in adjacency format.'''
    # Construct the trie.
    t = Trie(words)

    # Convert trie edges to adjacency form, as edges are currently dictionary items.
    # Converts: ((1, 2), 'A')  --> '1 2 A'
    adjacency_format = lambda item: ' '.join(map(str,item[0]))+' '+item[1]

    # Return all edges converted to adjacency form.
    return map(adjacency_format, t.edges.items())


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_7a.txt') as input_data:
        words = [line.strip() for line in input_data.readlines()]

    # Get the adjacency list.
    adjacency_list = trie_edges(words)

    # Print and save the answer.
    print '\n'.join(adjacency_list)
    with open('output/textbook/Textbook_07A.txt', 'w') as output_file:
        output_file.write('\n'.join(adjacency_list))

if __name__ == '__main__':
    main()
