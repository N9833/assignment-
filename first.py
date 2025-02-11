import numpy as np
import matplotlib.pyplot as plt

# Define different values of n
n_values = [500, 1000, 2000, 5000, 10000, 15000, 20000, 50000, 100000]

# Loop over each n value
for n in n_values:
    # Simulate rolling two fair dice n times
    dice1 = np.random.randint(1, 7, size=n)
    dice2 = np.random.randint(1, 7, size=n)
    s = dice1 + dice2  # Sum of both dice

    # Compute histogram
    h, h2 = np.histogram(s, bins=range(2, 14))

    # Normalize and plot
    plt.bar(h2[:-1], h/n)
    plt.title(f'Histogram of Dice Sums (n={n})')
    plt.xlabel('Sum')
    plt.ylabel('Frequency')
    plt.show()
