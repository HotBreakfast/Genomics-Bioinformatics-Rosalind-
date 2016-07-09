#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Multiple Pattern Matching Problem
Rosalind ID: 7B
URL: http://rosalind.info/problems/7b/
'''

from scripts import Trie


def trie_pattern_matching(word, patterns):
    '''Returns the starting index off all locations in word where a string in patterns is a substring.'''

    # Construct a trie from all of the given patterns.
    t = Trie(patterns)

    # Checck each index in the word (until the remainder is shorter than the shortest pattern)
    # to see if a pattern occurs starting at the specified index.
    check_patterns = [i for i in xrange(len(word)-min(map(len, patterns))+1) if t.prefix_in_trie(word[i:]) is True]

    return check_patterns


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_7b.txt') as input_data:
        word = input_data.readline().strip()
        patterns = [line.strip() for line in input_data.readlines()]

    # Get the matching pattern indices.
    pattern_indices = trie_pattern_matching(word, patterns)

    # Print and save the answer.
    print ' '.join(map(str, pattern_indices))
    with open('output/textbook/Textbook_07B.txt', 'w') as output_data:
        output_data.write(' '.join(map(str, pattern_indices)))

if __name__ == '__main__':
    main()
