#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook Track.

Problem Title: The Change Problem
Assignment #: 05
Problem ID: A
URL: http://rosalind.info/problems/5a/
'''


def dp_change(amount, coin_list):
    '''Gives the minimum number of coins of denomination in coint_list necessary to create the given amount.'''
    # Initiate the amounts larger than zero as a number greater than the upper bound.
    min_coins = [0]+[(amount/min(coin_list))+1]*amount

    # Use dynamic programming to build up to the desired amount.
    for m in xrange(1,amount+1):
        for coin in coin_list:
            if m >= coin:
                if min_coins[m-coin] + 1 < min_coins[m]:
                    min_coins[m] = min_coins[m-coin] + 1
    return min_coins[amount]


def main():
    '''Main call. Reads, runs, and saves problem specific data.'''
    # Read the input data.
    with open('data/textbook/rosalind_5a.txt') as input_data:
        amount = int(input_data.readline().strip())
        coin_list = map(int, input_data.readline().strip().split(','))

    # Get the desired minimum number of coins.
    min_number = str(dp_change(amount, coin_list))

    # Print and save the answer.
    print min_number
    with open('output/textbook/Textbook_05A.txt', 'w') as output_data:
        output_data.write(min_number)

if __name__ == '__main__':
    main()
