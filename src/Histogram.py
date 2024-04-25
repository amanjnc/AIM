import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/benin-malanville.csv')


variables_of_interest = ['GHI', 'DNI', 'DHI', 'WS', 'TModA', 'TModB']

fig, axes = plt.subplots(nrows=len(variables_of_interest), ncols=1, figsize=(8, 12))

for i, variable in enumerate(variables_of_interest):
    axes[i].hist(data[variable], bins=20, edgecolor='black')
    axes[i].set_xlabel(variable)
    axes[i].set_ylabel('Frequency')

plt.tight_layout()

plt.show()