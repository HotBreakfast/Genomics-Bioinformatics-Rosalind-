#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Longest Shared Repeat Problem
Rosalind ID: 7E
URL: http://rosalind.info/problems/7e/
'''

from scripts import GeneralizedSuffixTree


def longest_common_substring(string_list):
    '''Returns the longest common substring among all strings in string_list.'''
    # Construct the generalized suffix tree for the input text.
    gst = GeneralizedSuffixTree(string_list)

    # Find all nodes that are traversed by all words in text, meaning that the substring up to that node is in all words in text.
    candidate_nodes = filter(lambda i: len(gst.nodes[i].words) == len(string_list), xrange(len(gst.nodes)))

    # Get the deepest node of from the candidate nodes, where depth corresponds to substring length.
    deepest_node = max(candidate_nodes, key=lambda i: gst.node_depth(i))

    # Return the substring corresponding to a traversal up to the deepest node.
    return gst.node_substring(deepest_node)


def main():
    '''Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_7e.txt') as input_data:
        text = [line.strip() for line in input_data]

    # Get the longest shared repeat.
    longest_shared_repeat = longest_common_substring(text)

    # Print and save the answer.
    print longest_shared_repeat
    with open('output/textbook/Textbook_07E.txt', 'w') as output_data:
        output_data.write(longest_shared_repeat)

if __name__ == '__main__':
    main()
