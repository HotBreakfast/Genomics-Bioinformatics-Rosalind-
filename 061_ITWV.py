#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding Disjoint Motifs in a Gene
Rosalind ID: ITWV
Rosalind #: 061
URL: http://rosalind.info/problems/itwv/
'''


def check_interweave(dna1, dna2, superstr):
    '''Checks if two dna stands can be interwoven into a superstring.'''
    if len(superstr) == 0:
        return True
    elif dna1[0] == dna2[0] == superstr[0]:
        return check_interweave(dna1[1:], dna2, superstr[1:]) or check_interweave(dna1, dna2[1:], superstr[1:])
    elif dna1[0] == superstr[0]:
        return check_interweave(dna1[1:], dna2, superstr[1:])
    elif dna2[0] == superstr[0]:
        return check_interweave(dna1, dna2[1:], superstr[1:])
    else:
        return False

if __name__ == '__main__':
    from numpy import zeros

    # Read the input data.
    with open('data/rosalind_itwv.txt') as input_data:
        superstr = input_data.readline()
        dna = [line.strip() for line in input_data.readlines()]

    # Initialize the zero matrix.
    M = zeros((len(dna), len(dna)), dtype=int)

    # Run through all combinations of dna strings.
    for i in xrange(len(dna)):
        for j in xrange(len(dna)):
            if i <= j:
                # Count the combined number of each type of nucleotide in given dna strands.
                current_profile = [(dna[i]+dna[j]).count(nucleotide) for nucleotide in 'ACGT']
                # Compare the current profile to each substring of the same length in the superstring.
                for index in xrange(len(superstr)-len(dna[i])-len(dna[j])+1):
                    # Having an identical profile is a necessary condition in order to be interweavable, but less computationally intensive.
                    if current_profile == [superstr[index:index+len(dna[i])+len(dna[j])].count(nucleotide) for nucleotide in 'ACGT']:
                        # Check interweavability if the profiles match, add an extra character outside the alphabet to avoid index out of range errors.
                        if check_interweave(dna[i]+'$', dna[j]+'$', superstr[index:index+len(dna[i])+len(dna[j])]):
                            M[i][j] = 1
                            break
            # The comparison are symmetric, so we've already done these computations.
            else:
                M[i][j] = M[j][i]

    # Print and save the answer.
    print '\n'.join([' '.join(map(str, M[i])) for i in xrange(len(dna))])
    with open('output/061_ITWV.txt', 'w') as output_data:
        output_data.write('\n'.join([' '.join(map(str, M[i])) for i in xrange(len(dna))]))
