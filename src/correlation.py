import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('data/benin-malanville.csv')        


def correlation(CorrelatedMat):
    

    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', square=True)

    plt.title('Correlation Matrix')

    plt.tight_layout()

    plt.show()

columns_of_interest = ['GHI', 'TModA']
selected_data = data[columns_of_interest]
correlation_matrix = selected_data.corr()
correlation(correlation_matrix)