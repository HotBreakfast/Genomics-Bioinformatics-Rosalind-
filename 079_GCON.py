#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Global Alignment with Constant Gap Penalty
Rosalind ID: GCON
Rosalind #: 079
URL: http://rosalind.info/problems/gcon/
'''

from scripts import BLOSUM62, ReadFASTA


def global_alignment_with_constant_gap(v, w, scoring_matrix, sigma):
    '''Returns the global alignment score of v and w with constant gap peantaly sigma subject to the scoring_matrix.'''
    from numpy import zeros

    # Initialize the matrices.
    S_lower = zeros((len(v)+1, len(w)+1), dtype=int)
    S_middle = zeros((len(v)+1, len(w)+1), dtype=int)
    S_upper = zeros((len(v)+1, len(w)+1), dtype=int)

    # Initialize the edges with the given penalties.
    for i in xrange(1, len(v)+1):
        S_lower[i][0] = -sigma
        S_middle[i][0] = -sigma
        S_upper[i][0] = -10*sigma
    for j in xrange(1, len(w)+1):
        S_upper[0][j] = -sigma
        S_middle[0][j] = -sigma
        S_lower[0][j] = -10*sigma

    # Fill in the scores for the lower, upper, and middle matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            S_lower[i][j] = max([S_lower[i-1][j], S_middle[i-1][j] - sigma])
            S_upper[i][j] = max([S_upper[i][j-1], S_middle[i][j-1] - sigma])
            S_middle[i][j] = max([S_lower[i][j], S_middle[i-1][j-1] + scoring_matrix[v[i-1], w[j-1]], S_upper[i][j]])

    # Get the maximum score.
    max_score = S_middle[len(v)][len(w)]

    return max_score

if __name__ == '__main__':

    # Parse the two input protein strings.
    s, t = [fasta[1] for fasta in ReadFASTA('data/rosalind_gcon.txt')]

    # Get the alignment score.
    score = str(global_alignment_with_constant_gap(s, t, BLOSUM62(), 5))

    # Print and save the answer.
    print score
    with open('output/079_GCON.txt', 'w') as output_data:
        output_data.write(score)
