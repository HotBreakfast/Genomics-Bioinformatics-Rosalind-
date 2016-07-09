#!/usr/bin/env python
"""
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Frequent Words with Mismatches and Reverse Complements Problem
Chapter #: 01
Problem ID: H
URL: http://rosalind.info/problems/1h/
"""

from collections import defaultdict
from scripts import ReverseComplementDNA as rev_comp
from Textbook_01G import kmer_mismatches


def freq_words_with_mm_and_rev_comp(seq, k, d):
    """Returns all most frequent k-mers with up to d mismatches in the dna sequence seq."""
    # Frequency analysis so we don't generate mismatches for the same k-mer more than once.
    kmer_freq = defaultdict(int)
    for i in xrange(len(seq)-k+1):
        kmer_freq[seq[i:i+k]] += 1
        kmer_freq[rev_comp(seq[i:i+k])] += 1

    # Get all of the mismatches for each unique k-mer in the sequence, appearing freq times.
    mismatch_count = defaultdict(int)
    for kmer, freq in kmer_freq.iteritems():
        for mismatch in kmer_mismatches(kmer, d):
            mismatch_count[mismatch] += freq

    # Computing the maximum value is somewhat time consuming to repeat, so only do it once!
    max_count = max(mismatch_count.values())
    return sorted([kmer for kmer, count in mismatch_count.iteritems() if count == max_count])


def main():
    """Main call. Parses, runs, and saves problem specific data."""
    # Read the input data.
    with open('data/textbook/rosalind_1h.txt') as input_data:
        seq = input_data.readline().strip()
        k, d = map(int, input_data.read().strip().split())

    # Get the most frequent k-mers with up to d mismatches.
    most_freq_kmers = freq_words_with_mm_and_rev_comp(seq, k, d)

    # Print and save the answer.
    print ' '.join(most_freq_kmers)
    with open('output/textbook/Textbook_01H.txt', 'w') as output_data:
        output_data.write(' '.join(most_freq_kmers))

if __name__ == '__main__':
    main()
