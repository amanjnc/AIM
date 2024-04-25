import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('data/benin-malanville.csv')
variable_pairs = [('GHI', 'Tamb'), ('WS', 'WSgust'), ('Variable1', 'Variable2')]

for pair in variable_pairs:
    plt.scatter(data[pair[0]], data[pair[1]])
    plt.xlabel(pair[0])
    plt.ylabel(pair[1])
    plt.title(f'Scatter Plot: {pair[0]} vs. {pair[1]}')
    plt.show()