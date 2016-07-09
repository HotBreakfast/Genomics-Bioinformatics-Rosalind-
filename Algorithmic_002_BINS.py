#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Binary Search
Rosalind ID: BINS
Algorithmic Heights #: 002
URL: http://rosalind.info/problems/bins/
'''


def binary_search(A, to_find, start_index=None, stop_index=None):
    '''Performs a binary search on the sorted array A to return the index of to_find, or -1 if not present.'''

    start_index = 0 if start_index is None else start_index
    stop_index = len(A)-1 if stop_index is None else stop_index

    if stop_index < start_index:
        # The desired value is not present if we no longer have a region to search.
        return -1

    else:
        # Get the middle index of the current search range, rounding down if necessary.
        mid_index = (start_index + stop_index)/2

        if A[mid_index] > to_find:
            # Search the lower half of the current search range if the mid value is larger than the desired value.
            return binary_search(A, to_find, start_index, mid_index - 1)
        elif A[mid_index] < to_find:
            # Search the upper half of the current search range if the mid value is smaller than the desired value.
            return binary_search(A, to_find, mid_index + 1, stop_index)
        else:
            # If mid value is not larger or smaller then it must be exactly what we're looking for!
            return mid_index


if __name__ == '__main__':

    # Read the input data.
    with open('data/algorithmic/rosalind_bins.txt') as input_data:
        n, m = [int(input_data.readline().strip()) for repeat in xrange(2)]
        A = map(int, input_data.readline().strip().split())
        k = map(int, input_data.readline().strip().split())

    # Perform a binary search to find the desired indices.
    indices = [binary_search(A, k_i) for k_i in k]

    # Rosalind starts their indicies at 1 instead of 0, so shift all non-negative indices forward by one.
    indices = [str(index + 1) if index >= 0 else str(-1) for index in indices]

    # Print and save the answer.
    print ' '.join(indices)
    with open('output/algorithmic/Algorithmic_002_BINS.txt', 'w') as output_data:
        output_data.write(' '.join(indices))
