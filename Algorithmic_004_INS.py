#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Insertion Sort
Rosalind ID: INS
Algorithmic Heights #: 004
URL: http://rosalind.info/problems/ins/
'''


def insertion_sort(A):
    '''Performs the insertion sort algorithm. Returns the number of swaps performed in the sort.'''
    # Initialize the number of swaps.
    swaps = 0

    # Perform the insertion sort algorithm.
    for i in xrange(1, len(A)):
        while i > 0 and A[i] < A[i-1]:
            # Swap the indices if the condition holds.
            A[i-1], A[i] = A[i], A[i-1]
            i -= 1
            swaps += 1  # Problem wants us to count swaps.

    # The problem wants the number of swaps, not the actual sorted list.
    return swaps


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_ins.txt') as input_data:
        # We don't the first of the two lines.
        A = map(int, input_data.readlines()[1].strip().split())

    # Get the number of swaps.
    swaps = str(insertion_sort(A))

    # Print and save the answer.
    print swaps
    with open('output/algorithmic/Algorithmic_004_INS.txt', 'w') as output_data:
        output_data.write(swaps)

if __name__ == '__main__':
    main()
