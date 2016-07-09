#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Number of Breakpoints Problem
Rosalind ID: 6B
URL: http://rosalind.info/problems/6b/
'''


def breakpoint_count(permutation):
    '''Returns the number of breakpoints in a given permutation.'''

    # Prepend 0 and append len(permutation)+1 to check if the endpoints are in place.
    return sum(map(lambda x,y: x - y != 1, permutation+[len(permutation)+1], [0]+permutation))


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data/textbook/rosalind_6b.txt') as input_data:
        perm = map(int, input_data.read().strip().lstrip('(').rstrip(')').split())

    # Get the number of breakpoints
    num_of_breakpoints = breakpoint_count(perm)

    # Print and save the answer.
    print str(num_of_breakpoints)
    with open('output/textbook/Textbook_06B.txt', 'w') as output_data:
        output_data.write(str(num_of_breakpoints))

if __name__ == '__main__':
    main()
