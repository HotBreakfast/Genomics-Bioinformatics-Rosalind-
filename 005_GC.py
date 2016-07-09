#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Computing GC Content
Rosalind ID: GC
Rosalind #: 005
URL: http://rosalind.info/problems/gc/
'''
from scripts import ReadFASTA


def max_gc_content(seq_list):
    gc_content = lambda seq: sum([100.0 for base in seq if base in ('G', 'C')])/len(seq)  # 100 to scale result to %.
    gc_list = [[seq_name, gc_content(seq)] for seq_name, seq in seq_list]
    return max(gc_list, key=lambda x: x[1])


def main():
    '''Main call. Parses, runs, and saves problem specific data.'''
    # Parse the input data.
    seq_list = ReadFASTA('data/rosalind_gc.txt')
    highest_gc = map(str, max_gc_content(seq_list))

    # Print and save the answer.
    print '\n'.join(highest_gc)
    with open('output/005_GC.txt', 'w') as output_data:
        output_data.write('\n'.join(highest_gc))

if __name__ == '__main__':
    main()
