#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Merge Sort
Rosalind ID: MS
Algorithmic Heights #: 012
URL: http://rosalind.info/problems/ms/
'''
from Algorithmic_007_MER import merge_sorted_arrays


def merge_sort(A):
    '''Uses the merge sort algorithm to sort an array A.'''
    # Trivially sorted if the length is <= 1.
    # Also, this is used in the process of breaking down the array before rebuilding it sorted.
    if len(A) <= 1:
        return A

    # Get the midpoint of A.
    midpoint = len(A)/2

    # Use merge sort to sort the lower and upper halves of A.
    lower = merge_sort(A[:midpoint])
    upper = merge_sort(A[midpoint:])

    # Combine the sorted lower and upper halves.
    return merge_sorted_arrays(lower, upper)


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_ms.txt') as input_data:
        n = int(input_data.readline().strip())
        A = map(int, input_data.readline().strip().split())

    # Merge Sort array A.
    B = merge_sort(A)

    # Quick check of validity.
    assert B == sorted(A)

    # Print and save the answer.
    print ' '.join(map(str,B))
    with open('output/algorithmic/Algorithmic_012_MS.txt', 'w') as output_data:
        output_data.write(' '.join(map(str,B)))

if __name__ == '__main__':
    main()
