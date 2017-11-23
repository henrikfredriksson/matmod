#!/usr/bin/env python3

"""
Examples on how to plot using matplotlib

python3 -m pip install matplotlib numpy
"""

import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    This is the main method, I call it main by convention.
    """

    x = np.arange(-3*np.pi, 3*np.pi, 0.01)
    y = np.sin(x)/x

    plt.plot(x, y)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
