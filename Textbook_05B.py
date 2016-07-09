#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Manhattan Tourist
Assignment #: 05
Problem ID: B
URL: http://rosalind.info/problems/5b/
'''


def manhattan_tourist(n, m, down, right):
    '''Returns the longest path from (0,0) to (n,m) using the taxicab metric and weights down, right.'''
    # Initialize as the zero matrix.
    S = [[0]*(m+1) for i in xrange(n+1)]

    # Compute the first row and column.
    for i in xrange(1,n+1):
        S[i][0] = S[i-1][0] + down[i-1][0]
    for j in xrange(1, m+1):
        S[0][j] = S[0][j-1] + right[0][j-1]

    # Compute the interior values.
    for i in xrange(1,n+1):
        for j in xrange(1,m+1):
            S[i][j] = max(S[i-1][j]+down[i-1][j], S[i][j-1] + right[i][j-1])

    return S[n][m]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_5b.txt') as input_data:
        n, m = map(int, input_data.readline().strip().split())
        down, right = [[map(int, row.split()) for row in matrix.split('\n')] for matrix in input_data.read().strip().split('\n-\n')]

    # Get the maximum distance.
    max_dist = str(manhattan_tourist(n, m, down, right))

    # Print and save the answer.
    print max_dist
    with open('output/textbook/Textbook_05B.txt', 'w') as output_data:
        output_data.write(max_dist)

if __name__ == '__main__':
    main()
