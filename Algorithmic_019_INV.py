#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Counting Inversions
Rosalind ID: INV
Algorithmic Heights #: 019
URL: http://rosalind.info/problems/inv/
'''


def merge_sorted_arrays_counting_inversions(A, B):
    '''Merges two sorted arrays A and B into a sorted array C and counts the nmber of inversions.'''
    # Initialize variables.
    i, j = 0, 0
    count = 0
    C = []

    # Add the smallest item from A or B until one of the arrays runs out of items.
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            count += len(A) - i
            j += 1

    # Add on the additional items from the remaining array. (Only one will be nonempty)
    C += A[i:] + B[j:]

    return C, count


def merge_sort_inversion_count(A):
    '''Uses the merge sort algorithm to sort an array A and count inversions.'''
    # Trivially sorted if the length is <= 1.
    # Also, this is used in the process of breaking down the array before rebuilding it sorted.
    if len(A) <= 1:
        return A, 0

    # Get the midpoint of A.
    midpoint = len(A)/2

    # Use merge sort to sort the lower and upper halves of A.
    lower, lower_inv = merge_sort_inversion_count(A[:midpoint])
    upper, upper_inv = merge_sort_inversion_count(A[midpoint:])

    # Combine the sorted lower and upper halves.
    combined, combined_inv = merge_sorted_arrays_counting_inversions(lower, upper)

    return combined, lower_inv+upper_inv+combined_inv


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_inv.txt') as input_data:
        input_data.readline()
        A = map(int, input_data.readline().strip().split())
        # A = [1, 5, 4, 8, 10, 2, 6, 9, 12, 11, 3, 7]

    # Get the number of inversions.
    inversions = str(merge_sort_inversion_count(A)[1])

    # Print and save the answer.
    print inversions
    with open('output/algorithmic/Algorithmic_019_INV.txt', 'w') as output_data:
        output_data.write(inversions)

if __name__ == '__main__':
    main()
