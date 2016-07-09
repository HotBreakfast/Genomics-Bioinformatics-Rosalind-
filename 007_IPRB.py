#!/usr/bin/env python
"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Mendel's First Law
Rosalind ID: IPRB
Rosalind #: 007
URL: http://rosalind.info/problems/iprb/
"""

from scipy.misc import comb


def mendels_first_law(hom, het, rec):
    """
    Returns the probability that two radomly selected mating organisms will produce
    an individual possessing a dominant allele, assuming any two organisms can mate.
    hom = # of dominant mating organisms
    het = # of heterozygous mating organisms
    rec = # of recessive mating organisms.
    """
    # Compute the total number of possible children genotypes.
    # Note: Genotypes not necessarily unqiue. Factor of 4 due to four Punnett square child genotypes.
    total = 4*comb(hom+het+rec, 2)

    # Compute the total number of possible recessive child genotypes.
    # Rec x Rec -> All four Punnett square children recessive.
    # Rec x Het -> Two Punnett square children recessive.
    # Het x Het -> One Punnett suqare child recessive.
    # Dom x Any -> No receesive children.
    total_rec = 4*comb(rec, 2) + 2*rec*het + comb(het,2)

    # Use the complementary law of probability to get the probability of a dominant allete (i.e. Not Recessive):
    # P(Recessive) = #Recessive/#Total
    #  => P(Not Recessive) = 1 - #Recessive/#Total
    # Note: comb() returns float type, so we're fine doing division as is.
    return 1 - total_rec/total


def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Read the input data.
    with open('data/rosalind_iprb.txt') as input_data:
        k, m, n = map(int, input_data.read().strip().split())

    prob = str(mendels_first_law(k,m,n))

    # Print and save the answer.
    print prob
    with open('output/007_IRPB.txt', 'w') as output_data:
        output_data.write(prob)

if __name__ == '__main__':
    main()
