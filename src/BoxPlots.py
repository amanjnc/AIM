import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data/benin-malanville.csv')        
variables_of_interest = ['GHI', 'DNI', 'DHI', 'TModA', 'TModB', 'Tamb']
plt.figure(figsize=(10, 6)) 

data_to_plot = [data[var] for var in variables_of_interest]
plt.boxplot(data_to_plot, labels=variables_of_interest)

plt.xlabel('Variables')
plt.ylabel('Values')
plt.title('Box Plots of Solar Radiation and Temperature Data')

plt.show()