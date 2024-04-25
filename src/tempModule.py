import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/benin-malanville.csv')

variables_of_interest = ['TModA', 'TModB', 'Tamb']

for variable in variables_of_interest[:-1]:
    plt.scatter(data[variable], data['Tamb'], label=variable)

plt.xlabel('Module Temperature')
plt.ylabel('Ambient Temperature')
plt.title('Comparison of Module Temperature with Ambient Temperature')

plt.legend()

plt.show()