#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Sorting by Reversals
Rosalind ID: SORT
Rosalind #: 052
URL: http://rosalind.info/problems/sort/
'''


def breakpoint_count(permutation):
    '''Returns the number of breakpoints in a given permutation.'''

    # Prepend 0 and append len(permutation)+1 to check if the endpoints are in place.
    permutation = [0] + list(permutation) + [len(permutation)+1]

    return sum(map(lambda x,y: abs(x-y) != 1, permutation[1:], permutation[:-1]))


def breakpoint_indices(permutation):
    '''Returns the indices of all breakpoints in a given permutation.'''
    from itertools import compress
    # Prepend 0 and append len(permutation)+1 to check if the endpoints are in place.
    permutation = [0] + list(permutation) + [len(permutation)+1]

    return compress(xrange(len(permutation)-1), map(lambda x,y: abs(x-y) != 1, permutation[1:], permutation[:-1]))


def greedy_breakpoint_bfs_sort(permutation):
    '''Performs a greedy breakpoint reduction based BFS sorting of a given permutation.'''
    from itertools import product

    # Quick lambda function to reverse a region in the permutation.
    rev_perm = lambda perm, i, j: perm[:i] + perm[i:j+1][::-1] + perm[j+1:]

    # Initialize Variables
    permutation = tuple(permutation)
    current_perms = {permutation:[]}
    min_breaks = breakpoint_count(permutation)

    # Run the greedy BFS breakpoint reduction sorting.
    while True:
        new_perms = {}
        # Iterate over all combinations of breakpoint indices for all  current minimal permutations.
        for perm in current_perms.keys():
            for rev_ind in product(breakpoint_indices(perm), repeat=2):
                # Store some temporary variables for the given iteration.
                temp_perm = tuple(rev_perm(perm, rev_ind[0], rev_ind[1]-1))
                temp_breaks = breakpoint_count(temp_perm)
                temp_transformation = current_perms[perm] + [str(rev_ind[0]+1) + ' ' + str(rev_ind[1])]

                # Done we have no breakpoints.
                if temp_breaks == 0:
                    return temp_transformation

                # Create a new dictionary and update the minimum number of breakpoints if we've found a reduction.
                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = {temp_perm:temp_transformation}

                # Add to the dictionary if the current breakpoints match the minimum number.
                elif temp_breaks == min_breaks:
                    new_perms[temp_perm] = temp_transformation

        current_perms = new_perms


if __name__ == '__main__':

    # Read the input data.
    with open('data/rosalind_sort.txt') as input_data:
        perms = [map(int, line.strip().split()) for line in input_data.readlines()]

    # Normalize the permutations so that we sort to the identity permutation (1,2,3, ..., n).
    to_identity = {value:i+1 for i, value in enumerate(perms[1])}
    normalized_perm = [to_identity[value] for value in perms[0]]

    # Get the sorting.
    min_reversal = greedy_breakpoint_bfs_sort(normalized_perm)

    # Prepend the length of the sorting.
    min_reversal = [str(len(min_reversal))] + min_reversal

    # Print and save the answer.
    print '\n'.join(min_reversal)
    with open('output/052_SORT.txt', 'w') as output_data:
        output_data.write('\n'.join(min_reversal))
