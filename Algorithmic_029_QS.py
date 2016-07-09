#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Algorithmic Heights problem area.
Algorithmic Heights focuses on teaching algorithms and data structures commonly used in computer science.

Problem Title: Quick Sort
Rosalind ID: QS
Algorithmic Heights #: 029
URL: http://rosalind.info/problems/qs/
'''

from random import randint


def quicksort(a):
    '''Uses the quicksort algorithm to sort an array a.'''
    # Check that the list is trivally sorted.
    if len(a) <= 1:
        return a

    # Choose a pivot location and divide items into sets of less, equal, or greater.
    pivot = randint(0, len(a)-1)
    less, equal, greater = [], [], []
    for x in a:
        if x < a[pivot]:
            less.append(x)
        elif x == a[pivot]:
            equal.append(x)
        else:
            greater.append(x)

    # Quicksort the two unsorted sets.
    return quicksort(less) + equal + quicksort(greater)


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/algorithmic/rosalind_qs.txt') as input_data:
        input_data.readline()  # Skip first line.
        a = map(int, input_data.readline().strip().split())

    # Quicksort array a.
    b = quicksort(a)

    # Print and save the answer.
    print ' '.join(map(str,b))
    with open('output/algorithmic/Algorithmic_029_QS.txt', 'w') as output_data:
        output_data.write(' '.join(map(str,b)))

if __name__ == '__main__':
    main()
