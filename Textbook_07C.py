#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Longest Repeat Problem
Rosalind ID: 7C
URL: http://rosalind.info/problems/7c/
'''

# The problem statement says to use a suffix trie, but suffix trees are much more efficient.
from scripts import GeneralizedSuffixTree


def longest_repeat_substring(word, n):
    '''Returns the longest substring that appears at least n times in the given word.'''
    # Construct the suffix tree.
    gst = GeneralizedSuffixTree(word)

    # Find all nodes with at least n children.
    # The number of children a node has tells us how many times is associated substring appears within the string.
    candidate_nodes = filter(lambda i: len(gst.nodes[i].children) >= n, xrange(len(gst.nodes)))

    # Get the longest substring that appears at least n times.
    # Recall: node depth = proper length of substring, i.e. the length discounting the out of alphabet characters.
    best_node = max(candidate_nodes, key=lambda i: gst.node_depth(i))

    return gst.node_substring(best_node)


def main():
    '''Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_7c.txt') as input_data:
        text = input_data.read().strip()

    # Get the longest substring that appears more than once in the given string.
    longest_repeat = longest_repeat_substring(text, 2)

    # Print and save the answer.
    print longest_repeat
    with open('output/textbook/Textbook_07C.txt', 'w') as output_data:
        output_data.write(longest_repeat)

if __name__ == '__main__':
    main()
