#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Majority Element
Rosalind ID: MAJ
Algorithmic Heights #: 006
URL: http://rosalind.info/problems/maj/
'''


def majority_element(a):
    '''Uses Moore's Voting Algorithm to determine the majority element of an array a, if it exists.'''
    # Initialize the candidate element and count.
    candidate, count = a[0], 0
    # Run through the list, updating the count and changing candidates as necessary.
    for element in a:
        count += [-1, 1][element == candidate]
        if count == 0:
            candidate, count = element, 1

    # Check if the candidate is indeed the majority element, returning the appropriate result.
    return [-1, candidate][a.count(candidate) > len(a)/2]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_maj.txt') as input_data:
        next(input_data)  # Skip the first line, as we don't need that information.
        arrays = [map(int, line.strip().split()) for line in input_data]

    # Get the majority element of each array.
    maj_elmts = map(str, [majority_element(a) for a in arrays])

    # Print and save the answer.
    print ' '.join(maj_elmts)
    with open('output/algorithmic/Algorithmic_006_MAJ.txt', 'w') as output_data:
        output_data.write(' '.join(maj_elmts))

if __name__ == '__main__':
    main()
