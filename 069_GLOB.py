#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Global Alignment with Scoring Matrix
Rosalind ID: GLOB
Rosalind #: 069
URL: http://rosalind.info/problems/glob/
'''


def global_alignment_score(v, w, scoring_matrix, sigma):
    '''Return the global alignment score of v and w subject to the given scoring matrix and indel penalty sigma.'''

    # Initialize the scoring matrix.
    S = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]

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

    return S[len(v)][len(w)]

if __name__ == '__main__':
    from scripts import BLOSUM62, ReadFASTA

    # Parse the two input protein strings.
    s, t = [fasta[1] for fasta in ReadFASTA('data/rosalind_glob.txt')]

    # Get the alignment score.
    score = str(global_alignment_score(s, t, BLOSUM62(), 5))

    # Print and save the answer.
    print score
    with open('output/069_GLOB.txt', 'w') as output_data:
        output_data.write(score)
