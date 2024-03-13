#Lists and Modules
#Author: Addison
# 11 March 2024

import random

def coin_flip():
    # Return heads or tails or other?
    # Heads is any number 0 to 0.49999
    # Tails is any number from 0.5 to 0.99991
    # Other is any number greater thN 0.99991
    roll = random.random()

    if roll < 0.5:
        return "heads"
    elif roll <0.99991:
        return "tails"
    else:
        return "other?"


def card_reveal():
    # Reveal a "card" from A, 2, ..., Q, K
    roll = random.randrange(1, 14)  # (1, 14]

    if roll == 1:
        return "A"
    elif roll == 11:
        return "J"
    elif roll == 12:
        return "Q"
    elif roll == 13:
        return "K"
    else:
        return str(roll)

def main():
    # Keep track of heads and tails
    heads = 0
    tails = 0
    other = 0

    cards_drawn = []

    for _ in range(1_000):
        # Flip coin
        result = coin_flip()
        cards_drawn.append(card_reveal())

        if result == "heads":
            heads = heads + 1  # increment
        elif result == "tails":
            tails += 1  # increment
        else:
            other += 1

    print(cards_drawn)

    # Print results
    print(f"Number of Heads: {heads}")
    print(f"Number of Tails: {tails}")
    print(f"Number of Other: {other}")


main()    
    