#!/usr/bin/env python3

"""
Examples on how to plot using matplotlib

Plot the relative frequency value of a dice

python3 -m pip install matplotlib numpy
"""

import numpy as np
import matplotlib.pyplot as plt

def main():
    """
    This is the main method, I call it main by convention.
    """

    dice_rolls = 10000
    rel_freq = []
    cumulative_value = 0

    for i in range(1, dice_rolls):
        value = np.random.randint(1, 7)
        cumulative_value = cumulative_value + value
        rel_freq.append(cumulative_value/i)



    plt.plot(rel_freq, 'g-')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
