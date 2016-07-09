#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: 3-Way Partition
Rosalind ID: PAR3
Algorithmic Heights #: 020
URL: http://rosalind.info/problems/par3/
'''


def three_way_partition(a):
    '''Performs a 3-way partition on the array a.'''
    # Trivial with list comprehensions.
    return [x for x in a if x < a[0]] + [a[0]]*a.count(a[0]) + [x for x in a if x > a[0]]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_par3.txt') as input_data:
        input_data.readline()  # Don't need the first line.
        a = map(int, input_data.readline().strip().split())

    # Perform the 3-way partition.
    a = map(str, three_way_partition(a))

    # Print and save the answer.
    print ' '.join(a)
    with open('output/algorithmic/Algorithmic_020_PAR3.txt', 'w') as output_data:
        output_data.write(' '.join(a))


if __name__ == '__main__':
    main()
