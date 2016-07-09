#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Maximizing the Gap Symbols of an Optimal Alignment
Rosalind ID: MGAP
Rosalind #: 083
URL: http://rosalind.info/problems/mgap/
'''
# ---------------------------------------------------------------------------------------------
# SOLUTION COMMENTS AND EXPLANATION
# ---------------------------------------------------------------------------------------------
# This solution deserves more explanation than simple code comments, as the method to solve
# the problem seemingly has nothing to do with what is stated in the problem statement.
#
# The key thing to notice in the problem statement is that we want an optimal alignment
# and that there is no upper bound on the score associated with a match.  Thus, we can
# assign an arbitrarily high score to matches and ensure that the maximum score corresponds
# to aligning the maximum number of symbols.
#
# The maximum number of aligned symbols between two sequences is precisely the longest common
# subsequence, and determining the longest common subsequence is a problem that we've already
# solved on Rosalind (it is a prerequiste problem for this one!).
#
# Now, since we have a free choice on the penalties associated with mismatches and gaps,
# choose a lowerpenalty for gaps, and match all non-longest subsequence symbols with gaps.
# Thus, we have one gap symbol for each nucleotide that is no part of the longest common
# subsequence in each problem.
#
# So: max #Gaps = |seq1| + |seq2| - 2*|longest subsequence|
# ---------------------------------------------------------------------------------------------

from scripts import ReadFASTA


def maximum_gap_symbols(v, w):
    '''Returns the max number of gap symbols in an optimal alignment of v and w.'''
    # Get the length of the longest common subsequence.
    M = [[0 for j in xrange(len(w)+1)] for i in xrange(len(v)+1)]
    for i in xrange(len(v)):
        for j in xrange(len(w)):
            if v[i] == w[j]:
                M[i+1][j+1] = M[i][j]+1
            else:
                M[i+1][j+1] = max(M[i+1][j],M[i][j+1])

    # Apply the aforementioned formula with the length of the longest subsequence.
    return len(v) + len(w) - 2*M[len(v)][len(w)]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Parse the input data.
    v, w = [fasta[1] for fasta in ReadFASTA('data/rosalind_mgap.txt')]

    # Get the maximum number of gaps.
    max_gaps = str(maximum_gap_symbols(v,w))

    # Print and save the answer.
    print max_gaps
    with open('output/083_MGAP.txt', 'w') as output_data:
        output_data.write(max_gaps)

if __name__ == '__main__':
    main()
