#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Overlap Alignment
Rosalind ID: OAP
Rosalind #: 098
URL: http://rosalind.info/problems/oap/
'''


def overlap_alignment(v, w):
    '''Returns the overlap alignment of strings v and w.'''

    # Initialize the arrays.
    S = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]
    backtrack = [[0 for repeat_j in xrange(len(w)+1)] for repeat_i in xrange(len(v)+1)]

    # Initialize the max score.
    max_score = -3*(len(v) + len(w))

    # Fill in the Score and Backtrack arrays.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            # Match score = 1, Mismatch and Indels = -2.
            scores = [S[i-1][j-1] + [-2, 1][v[i-1] == w[j-1]], S[i-1][j] - 2, S[i][j-1] - 2]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

            # Check if we have a new maximum along the last row or column and update accordingly.
            if i == len(v) or j == len(w):
                if S[i][j] > max_score:
                    max_score = S[i][j]
                    max_indices = (i, j)

    # Initialize i and j as their corresponding index of the maximum score.
    i, j = max_indices

    # Initialize the aligned strings as the input strings, removing the unused tails.
    v_aligned, w_aligned = v[:i], w[:j]

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Backtrack to the first row or column from the highest score in the last row or column.
    while i*j != 0:
        if backtrack[i][j] == 1:
            i -= 1
            w_aligned = insert_indel(w_aligned, j)
        elif backtrack[i][j] == 2:
            j -= 1
            v_aligned = insert_indel(v_aligned, i)
        else:
            i -= 1
            j -= 1

    # Remove the unused head the aligned strings.
    v_aligned, w_aligned = v_aligned[i:], w_aligned[j:]

    return str(max_score), v_aligned, w_aligned


if __name__ == '__main__':
    from scripts import ReadFASTA

    # Parse the two input dna strings.
    s, t = [fasta[1] for fasta in ReadFASTA('data/rosalind_oap.txt')]

    # Get the overlap alignment.
    alignment = overlap_alignment(s, t)

    # Print and save the answer.
    print '\n'.join(alignment)
    with open('output/098_OAP.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))
