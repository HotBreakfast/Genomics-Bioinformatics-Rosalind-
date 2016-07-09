#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Semiglobal Alignment
Rosalind ID: SMGB
Rosalind #: 101
URL: http://rosalind.info/problems/smgb/
'''

from scripts import ReadFASTA


def semiglobal_alignment(v, w, sigma):
    '''Returns the semiglobal alignment of v and w and the associated score.'''
    # Initialize the matrices.
    S = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    backtrack = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]

    # Fill in the Score and Backtrack matrices.
    for i in xrange(1, len(v)+1):
        for j in xrange(1, len(w)+1):
            scores = [S[i-1][j] - sigma, S[i][j-1] - sigma, S[i-1][j-1] + [-1, 1][v[i-1] == w[j-1]]]
            S[i][j] = max(scores)
            backtrack[i][j] = scores.index(S[i][j])

    # Get the position of the highest scoring cell in the last row or last column.
    last_row_index = max(xrange(len(w)+1), key=lambda x: S[len(v)][x])
    last_column_index = max(xrange(len(v)+1), key=lambda x: S[x][len(w)])
    if S[len(v)][last_row_index] >= S[last_column_index][len(w)]:
        i = len(v)
        j = last_row_index
    else:
        i = last_column_index
        j = len(w)
    max_score = S[i][j]

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Initialize the aligned strings as the input strings.
    v_aligned, w_aligned = v, w

    # Append indels as necessary.
    for _ in xrange(len(v) - i):
        w_aligned += '-'
    for _ in xrange(len(w) - j):
        v_aligned += '-'

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

    return str(max_score), v_aligned, w_aligned


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read and parse the input data.
    word1, word2 = [fasta[1] for fasta in ReadFASTA('data/rosalind_smgb.txt')]

    # Get the alignment.
    alignment = semiglobal_alignment(word1, word2, 1)

    # Print and save the answer.
    print '\n'.join(alignment)
    with open('output/101_SMGB.txt', 'w') as output_data:
        output_data.write('\n'.join(alignment))

if __name__ == '__main__':
    main()
