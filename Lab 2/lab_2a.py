# -*- coding: utf-8 -*-
"""
@author: Lexzander Saplan
@author: David Ibarra

EE 381 : Lab Project 2 - Part A
Professor Sam Jalali
"""

import numpy as np

def number_of_changes(coins, flips, probabilities):
    """
    Chooses random coins using respective probabilities and number of flips
    coins - Array holding possible choices (coins)
    flips - Number of trials to perform
    p     - Probability of getting respective choice (i.e. H = 0.5 / T = 0.5)
    """
    simulated_flips = np.random.choice(coins, flips, probabilities)

    # Prints coins for simulated number of flips
    print(simulated_flips)

    # Keeps count of changes in coin face (H / T)
    changes = 0
    # Retrieve first coin (This coin cannot be compared because it is first)
    current_coin = simulated_flips[0]
    # Starting with the second coin, loop through all the simulated flips
    for coin in simulated_flips[1:]:
        # Check if the current coin is not the same
        if current_coin != coin:
            # Increment a face change
            changes += 1
            # Make the current coin the new face of the coin
            current_coin = coin
    
    # Return the number of changes
    return changes


def main():
    # Number of flips
    n = 10

    # Possible choices (H / T.)
    coins = ["H", "T"]

    # ---------------------------------------------------------------- #

    # Part 1
    print("Simulation for", n, "flips with P(H) = 1/2")

    # p - Respective probabilties for choosing a coin
    # P(H) = 1/2 , P(T) = 1/2
    p = [1/2, 1/2]
    changes = number_of_changes(coins, n, p)
    print(changes, "changes out of", n, "flips")

    # ---------------------------------------------------------------- #

    # Part 2
    print("\nSimulation for", n, "flips with P(H) = 1/3")

    # p - Respective probabilties for choosing a coin
    # P(H) = 1/3 , P(T) = 2/3
    p = [1/3, 2/3]
    changes = number_of_changes(coins, n, p)
    print(changes, "changes out of", n, "flips")


main()
