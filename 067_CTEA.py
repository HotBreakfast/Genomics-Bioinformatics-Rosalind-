#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Optimal Alignments
Rosalind ID: CTEA
Rosalind #: 067
URL: http://rosalind.info/problems/ctea/
'''

from scripts import ReadFASTA


def count_alignment(v, w):
    '''Returns the number of optimal edit alignments of strings v and w.'''
    from numpy import zeros

    # Initialize the matrices and modulus.
    S = zeros((len(v)+1, len(w)+1), dtype=int)
    dynamic_count = zeros((len(v)+1, len(w)+1), dtype=int)
    modulus = 2**27 - 1  # It may be a good idea to only compute this once...

    # Initialize the first row and column of the matrices.
    for i in xrange(0, len(v)+1):
        S[i][0] = i
        dynamic_count[i][0] = 1
    for j in xrange(1, len(w)+1):
        S[0][j] = j
        dynamic_count[0][j] = 1

    # Fill in the Score and Dynamic Count matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            # Get the score for each possible alignment at the given iteration.
            scores = [S[i-1][j-1] + (v[i-1] != w[j-1]), S[i-1][j]+1, S[i][j-1]+1]
            S[i][j] = min(scores)

            # Add the preceeding number of alignments if the score matches the minumum score.
            dynamic_count[i][j] += [0, dynamic_count[i-1][j-1]][scores[0] == S[i][j]]
            dynamic_count[i][j] += [0, dynamic_count[i-1][j]][scores[1] == S[i][j]]
            dynamic_count[i][j] += [0, dynamic_count[i][j-1]][scores[2] == S[i][j]]

            # Take the count modulo 2**27 - 1.
            dynamic_count[i][j] = dynamic_count[i][j] % modulus

    return dynamic_count[len(v)][len(w)]

if __name__ == '__main__':

    # Parse the two input protein strings.
    s, t = [fasta[1] for fasta in ReadFASTA('data/rosalind_ctea.txt')]

    # Get number of optimal alignments.
    count = str(count_alignment(s, t))

    # Print and save the answer.
    print count
    with open('output/067_CTEA.txt', 'w') as output_data:
        output_data.write(count)
