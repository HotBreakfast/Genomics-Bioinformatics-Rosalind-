#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Edit Distance
Assignment #: 05
Problem ID: G
URL: http://rosalind.info/problems/5g/
'''


def edit_distance(v,w):
    '''Returns the edit distance of strings v and w.'''
    # Initialize matrix M.
    M = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    for i in range(1,len(v)+1):
        M[i][0] = i
    for j in range(1,len(w)+1):
        M[0][j] = j

    # Compute each entry of M.
    for i in xrange(1,len(v)+1):
        for j in xrange(1,len(w)+1):
            if v[i-1] == w[j-1]:
                M[i][j] = M[i-1][j-1]
            else:
                M[i][j] = min(M[i-1][j]+1, M[i][j-1]+1, M[i-1][j-1]+1)

    # Print and save the desired edit distance.
    return M[len(v)][len(w)]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_5g.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the edit distance.
    e_dist = edit_distance(word1, word2)

    # Print and save the answer.
    print str(e_dist)
    with open('output/textbook/Textbook_05G.txt', 'w') as output_data:
        output_data.write(str(e_dist))

if __name__ == '__main__':
    main()
