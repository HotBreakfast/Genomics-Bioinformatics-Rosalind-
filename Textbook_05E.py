#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: Global Alignment
Assignment #: 05
Problem ID: E
URL: http://rosalind.info/problems/5e/
'''

from scripts import BLOSUM62


def global_alignment(v, w, scoring_matrix, sigma):
    '''Returns the global alignment of v and w subject to the given scoring matrix and indel penalty sigma.'''
    # Initialize the matrices.
    S = [[0]*(len(w)+1) for _ in xrange(len(v)+1)]
    backtrack = [[0]*(len(w)+1) for _ in xrange(len(v)+1)]

    # Initialize the edges with the given penalties.
    for i in xrange(1, len(v)+1):
        S[i][0] = -i*sigma
    for j in xrange(1, len(w)+1):
        S[0][j] = -j*sigma

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    v_aligned, w_aligned = v, w

    # Get the position of the highest scoring cell in the matrix and the high score.
    i, j = len(v), len(w)
    max_score = str(S[i][j])

    # Backtrack to the edge of the matrix starting at the highest scoring cell.
    while i*j != 0:
        if backtrack[i][j] == 0:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 1:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    # Prepend the necessary preceeding indels to get to (0,0).
    for _ in xrange(i):
        w_aligned = insert_indel(w_aligned, 0)
    for _ in xrange(j):
        v_aligned = insert_indel(v_aligned, 0)

    return max_score, v_aligned, w_aligned


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_5e.txt') as input_data:
        word1, word2 = [line.strip() for line in input_data.readlines()]

    # Get the alignment.
    alignment = global_alignment(word1, word2, BLOSUM62(), 5)

    # Print and save the answer.
    print '\n'.join(alignment)
    with open('output/textbook/Textbook_05E.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))

if __name__ == '__main__':
    main()
