#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Merge Two Sorted Arrays
Rosalind ID: MER
Algorithmic Heights #: 007
URL: http://rosalind.info/problems/mer/
'''


def merge_sorted_arrays(A, B):
    '''Merges two sorted arrays A and B into a sorted array C.'''

    # Initialize variables.
    i, j = 0, 0
    C = []

    # Add the smallest item from A or B until one of the arrays runs out of items.
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1

    # Add on the additional items from the remaining array. (Only one will be nonempty)
    C += A[i:] + B[j:]

    return C


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''

    # Read the input data.
    with open('data/algorithmic/rosalind_mer.txt') as input_data:
        n, A, m, B = [int(line.strip()) if i % 2 == 0 else map(int, line.strip().split()) for i, line in enumerate(input_data.readlines())]

    # Merge sorted arrays A and B.
    C = merge_sorted_arrays(A, B)

    # Print and save the answer.
    print ' '.join(map(str,C))
    with open('output/algorithmic/Algorithmic_007_MER.txt', 'w') as output_data:
        output_data.write(' '.join(map(str,C)))

if __name__ == '__main__':
    main()
